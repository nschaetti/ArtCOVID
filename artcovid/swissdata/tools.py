#
# This file is part of the ArtCovid distribution (https://github.com/nschaetti).
# Copyright (c) 2021 Nils Schaetti.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

# Imports
from typing import Dict, Any, List, Union
import numpy as np
import requests
import urllib.request
import json
import os
import zipfile
import h5py
import shutil
import copy

# Imports local
from artcovid.constants import SWISSDATA_CONTEXT
from artcovid.data_retrieval import create_dataset_directory
from artcovid.data_file import read_csv
from artcovid.swissdata import SWISSDATA_SCHEMA_FILES, SWISSDATA_DATA_DESCRIPTION


# Get model
def sw_get_model_name(
        data_file_name: str
) -> Union[str, None]:
    r"""Get model from data file.

    :param data_file_name: Name of the data (CSV) file
    :type data_file_name: str
    :return: Data definition or None.
    :rtype: str or None
    """
    if data_file_name in SWISSDATA_SCHEMA_FILES:
        return SWISSDATA_SCHEMA_FILES[data_file_name]
    else:
        return None
    # end if
# end swissdata_get_model_name


# Get column type
def sw_get_model_properties(
        swissdata_path: str,
        data_file_name: str
) -> Dict:
    r"""Get column type for the SwissData dataset in sources.schema.json.

    :param swissdata_path: Path to the SwissData directory.
    :param data_file_name: Name of the data (CSV) file.
    :return:
    """
    with open(os.path.join(swissdata_path, "sources.schema.json"), 'r') as schema_file:
        # Load JSON
        schema_data = json.load(schema_file)

        # Get model name
        data_model_name = sw_get_model_name(data_file_name)

        # Get model
        data_model = schema_data["definitions"][data_model_name]

        # Return model's properties
        return data_model['properties']
    # end with


# end swissdata_get_model_properties


# Create enum dictionary
def sw_create_enum_dict(
        column_desc: Dict
) -> Union[Dict, None]:
    r"""

    :param column_desc:
    :return:
    """
    if 'enum' in column_desc:
        enum_dict = {el.lower(): list.index(column_desc['enum'], el) + 1 for el in column_desc['enum']}
        enum_dict['unknown'] = 0
        enum_dict['NA'] = -1
        return enum_dict
    else:
        return None
    # end if


# end create_enum_dict


def sw_schema_type_to_h5(
        field_desc: Dict
) -> str:
    r"""

    :param field_desc:
    :return:
    """
    # Data title and type
    col_type = field_desc['ptype']

    # H5 Types
    if col_type == "enum":
        # Return special enum type
        return h5py.special_dtype(enum=("i", field_desc["values"]))
    elif col_type == "date" or col_type == "datetime" or col_type == "s":
        return h5py.string_dtype(encoding="utf-8")
    else:
        return field_desc['ptype']
    # end if


# end schema_type_to_h5


# Convert data
def sw_convert_data(
        data: str,
        field_desc: Dict
) -> Any:
    r"""Convert an entry to a numpy data.

    :param field_desc: The description of the field.
    :param data: The data to convert from the CSV.
    :return: The converted data.
    """
    # Data title and type
    col_type = field_desc['ptype']

    # Convert
    if col_type == "enum":
        if data == '' or data == 'NA':
            return -1
        else:
            if data not in field_desc['values']:
                return field_desc['values']['na']
            else:
                return field_desc['values'][data]
            # end if
        # end if
    else:
        if col_type == 'i':
            if data == 'NA' or data == '':
                return None
            else:
                return int(data)
            # end if
        elif col_type == 'f':
            if data == 'NA' or data == '':
                return np.nan
            else:
                return float(data)
            # end if
        elif col_type == 's' or col_type == 'date' or col_type == 'datetime':
            return data.encode('utf-8')
        elif col_type == 'b':
            return True if data == 'TRUE' else False
        # end if
    # end if

    # Error
    raise Exception("Unknown data type {}".format(col_type))
# end convert_data


# Construct array type
def sw_construct_array_type(
        header_names: List[str],
        fields_desc: Dict,
) -> np.dtype:
    r"""Construct the definition of the numpy array.

    :param header_names: Names of the columns in the header.
    :param fields_desc: The description of the field.
    :return: The definition of the numpy array as a numpy dtype.
    """
    # Types
    type_list = list()
    col_names = list()

    # List of column names
    for col_name in header_names:
        if col_name in fields_desc:
            type_list.append(sw_schema_type_to_h5(fields_desc[col_name]))
            col_names.append(col_name)
        # end if
    # end for

    return np.dtype({
        'names': col_names,
        'formats': type_list
    })
# end construct_array_type


# Validate column description
def sw_validate_column_descs(
        column_names: List[str],
        column_types: Dict
) -> Dict:
    r"""Validate column descriptions

    :param column_names:
    :param column_types:
    :return:
    """
    # List of column desc
    column_descs = {}

    # For each column
    for col_i, column_name in enumerate(column_names):
        # Get description if present, otherwise create
        if column_name in column_types:
            column_descs[column_name] = column_types[column_name]
            column_descs[column_name]['ctype'] = sw_schema_type_to_h5(column_descs[column_name])
        else:
            column_descs[column_name] = {
                'description': 'column not in schema',
                'title': column_name,
                'type': 'string',
                'ctype': h5py.string_dtype(encoding='utf-8')
            }
        # end if
    # end for

    return column_descs
# end validate_column_desc


# Merge two dicts
def sw_merge_dicts(
        dict_a: Dict,
        dict_b: Dict
) -> Dict:
    r"""Merge two dicts

    :param log_info:
    :param dict_a:
    :param dict_b:
    :return:
    """
    # For each items in b
    for k, v in dict_b.items():
        if k not in dict_a:
            dict_a[k] = v
        elif type(v) is dict:
            dict_a[k] = sw_merge_dicts(dict_a[k], dict_b[k])
        # end if
    # end for

    return dict_a
# end swissdata_merge_dicts


# Merge data descriptor and information from sources.schema.json
def sw_merge_description(
        swissdata_dir: str,
        data_desc: Dict,
        data_model_name: str
) -> Dict:
    r"""Merge data descriptor and information from sources.schema.json

    :param swissdata_dir: Path to the SwissData directory.
    :param data_desc: The description of the data (as dict).
    :param data_model_name: The name of the data model.
    :return: The new data description merged with information from sources.schema.json.
    """
    # Open sources.schema.json
    with open(os.path.join(swissdata_dir, "sources.schema.json"), 'r') as ssj_file:
        # Load JSON
        sources_schema = json.load(ssj_file)

        # Get the definition
        data_def = sources_schema['definitions'][data_model_name]

        # Merge dict
        return sw_merge_dicts(data_desc, data_def)
    # end with
# end swissdata_merge_description


# Extract models definitions from CSV file
def extract_models_definitions(
        data_dir: str,
        models_definitions: Dict
) -> Dict:
    r"""

    :param data_dir:
    :param models_definitions:
    :return:
    """
    # SwissData data directory
    swissdata_dir = os.path.join(data_dir, "swissdata")
    swissdata_data_dir = os.path.join(swissdata_dir, "data")

    # SwissData models definition
    models_definitions['definitions']['swissdata'] = {
        "$id": "https://covid19.admin.ch",
    }

    # List CSV files
    for csv_file_name in os.listdir(swissdata_data_dir):
        # Get model
        data_model_name = sw_get_model_name(csv_file_name[:-4])

        # Validate columns description
        if data_model_name in SWISSDATA_DATA_DESCRIPTION:
            # Get fields description
            data_desc = copy.deepcopy(SWISSDATA_DATA_DESCRIPTION[data_model_name])

            # Merge data description with source schema
            data_desc = sw_merge_description(swissdata_dir, data_desc, data_model_name)

            # Keep definitions
            models_definitions['definitions']['swissdata'][data_model_name] = data_desc
        # end if
    # end for

    return models_definitions
# end extract_models_definitions


# Convert swiss dataset
def swissdata_dataset_to_h5(
        data_dir: str,
        h5_group: h5py.Group,
        models_definitions: Dict
) -> Dict:
    r"""Convert the SwissData dataset to H5 file format.

    :param models_definitions:
    :param data_dir:
    :type data_dir:
    :param h5_group:
    :type h5_group:
    :return: New model definition dictionary.
    """
    # SwissData data directory
    swissdata_dir = os.path.join(data_dir, "swissdata")
    swissdata_data_dir = os.path.join(swissdata_dir, "data")

    # List CSV files
    for csv_file_name in os.listdir(swissdata_data_dir):
        # Read CSV
        header_row, rows_list = read_csv(os.path.join(swissdata_data_dir, csv_file_name))

        # Get model
        data_model_name = sw_get_model_name(csv_file_name[:-4])

        # Validate columns description
        if data_model_name in SWISSDATA_DATA_DESCRIPTION:
            # Get column types
            schema_file_desc = sw_get_model_properties(swissdata_dir, csv_file_name[:-4])

            # Get fields description
            data_desc = SWISSDATA_DATA_DESCRIPTION[data_model_name]

            # Merge data description with source schema
            data_desc = sw_merge_description(swissdata_dir, data_desc, data_model_name)

            # Model properties
            model_properties = data_desc['properties']

            # Compute types and create dataset in the file group
            print("\t\tConverting CSV file {}, with data model {}".format(csv_file_name, data_model_name))

            # Construct the numpy data type for the array
            ds_ctype = sw_construct_array_type(header_row, model_properties)

            # Get all data as a list
            data_list = [
                tuple([
                    sw_convert_data(row[col_i], model_properties[col_name])
                    for col_i, col_name in enumerate(header_row)
                    if col_name in model_properties
                ])
                for row in rows_list
            ]

            # Convert data
            ds_data = np.array(data_list, dtype=ds_ctype)

            # Create the dataset
            print("\t\tCreate a dataset {} for data".format(csv_file_name[:-4]))
            col_dataset = h5_group.create_dataset(
                csv_file_name[:-4],
                shape=(len(rows_list),),
                dtype=ds_ctype,
                data=ds_data
            )
            col_dataset.set_fill_value = np.nan

            # Set attributes
            for col_i, column_name in enumerate(header_row):
                if column_name in schema_file_desc:
                    # Set attributes
                    for p, v in schema_file_desc[column_name].items():
                        col_dataset.attrs[column_name + "_" + p] = v
                    # end fir
                # end if
            # end for

            # Keep definitions
            models_definitions['definitions']['swissdata'][data_model_name] = data_desc
        # end if
    # end for

    # Print info
    print("\tH5 group: {}".format(h5_group))

    return models_definitions
# end sw_convert_swiss_dataset


# Clean dataset directory
def clean_dataset_directory(
        data_dir: str
) -> None:
    r"""Remove schema and README, and move CSV to base directory.

    :param data_dir:
    :return:
    """
    # SwissData data directory
    swissdata_dir = os.path.join(data_dir, "swissdata")
    swissdata_data_dir = os.path.join(swissdata_dir, "data")

    # Remove json and md
    os.remove(os.path.join(swissdata_dir, "README.md"))
    os.remove(os.path.join(swissdata_dir, "sources.schema.json"))

    # Move all files in data to base
    for csv_file_name in os.listdir(swissdata_data_dir):
        # Dest. file name
        orig_file_name = os.path.join(swissdata_data_dir, csv_file_name)
        dest_file_name = os.path.join(swissdata_dir, csv_file_name)

        # Remove if exists
        if os.path.exists(dest_file_name):
            os.remove(dest_file_name)
        # end if

        # Move file
        shutil.move(orig_file_name, swissdata_dir)
    # end for

    # Remove data dir
    os.rmdir(swissdata_data_dir)
# end clean_dataset_directory


# Download Swiss Data dataset
def download_swissdata_dataset(
        dest_dir: str
) -> None:
    r"""Download the dataset from SwissData.

    :param dest_dir: Destination directory for CSV file.
    """
    # SwissData directory
    swissdata_dir = os.path.join(dest_dir, "swissdata")

    # Create if not exists
    create_dataset_directory(swissdata_dir)

    # Temporary zip file
    temp_zip_file = os.path.join(swissdata_dir, "swissdata_data.zip")

    # Load JSON
    with urllib.request.urlopen(SWISSDATA_CONTEXT) as url:
        # Log
        print("\t\tDownloading context at {}".format(SWISSDATA_CONTEXT))

        # Load data
        data = json.loads(url.read().decode())

        # CSV zip
        csv_zip = data['sources']['zip']['csv']
    # end with

    # Download CSV zip
    with open(temp_zip_file, 'wb') as sw_file:
        # Log
        print("\t\tDownloading CSV zip file at {}".format(csv_zip))

        # Request
        r = requests.get(csv_zip, allow_redirects=True)

        # Write
        sw_file.write(r.content)
    # end with

    # Unzip file
    with zipfile.ZipFile(temp_zip_file, "r") as zip_ref:
        # Log
        print("\t\tExtract zip file {} to {}".format(temp_zip_file, swissdata_dir))

        # Extract
        zip_ref.extractall(swissdata_dir)
    # end with

    # Delete zip file
    os.remove(temp_zip_file)
# end download_swissdata_dataset
