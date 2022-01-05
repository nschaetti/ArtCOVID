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
from typing import Dict
import h5py
import pandas as pd
import json
import os

# Imports ArtCOVID
import artcovid.swissdata as sw


# Split datetime field
def split_datetime_field(
        df: pd.DataFrame,
        prop_name: str,
) -> pd.DataFrame:
    r"""

    :return:
    """
    # Create year
    df[prop_name + "_year"] = pd.Categorical(
        values=df[prop_name].dt.year,
        categories=list(range(2019, 2023))
    )

    # and month
    df[prop_name + "_month"] = pd.Categorical(
        values=df[prop_name].dt.month,
        categories=list(range(1, 13))
    )

    # and day of month
    df[prop_name + "_day_of_month"] = pd.Categorical(
        values=df[prop_name].dt.day,
        categories=list(range(1, 32))
    )

    # day of week
    df[prop_name + "_dayofweek"] = pd.Categorical(
        values=df[prop_name].dt.dayofweek,
        categories=list(range(0, 7))
    )

    # day of week
    df[prop_name + "_day_name"] = pd.Categorical(
        values=df[prop_name].dt.day_name(),
        categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )
# end split_datetime_field


# Load models definitions
def load_models_definitions(
    dataset_root: str
) -> Dict:
    r"""Load models definitions.

    :param dataset_root:
    :return:
    """
    with open(os.path.join(dataset_root, "artcovid.schema.json"), 'r') as md_fd:
        # Load JSON
        return json.load(md_fd)
    # end with
# end load_models_definitions


# Load data
def load_dataset(
        dataset_root: str,
        dataset_name: str,
        collection_name: str,
) -> pd.DataFrame:
    r"""Load data from the root directory and return a Pandas DataFrame.

    :param dataset_root: Path to the root directory of the ArtCOVID dataset.
    :param dataset_name: Name of the dataset to load.
    :param collection_name: Name of the collection to load.
    :return: A Pandas DataFrame.
    """
    # Models definitions
    models_definitions = load_models_definitions(dataset_root)

    # Get model name
    if dataset_name == "swissdata":
        model_name = sw.SWISSDATA_SCHEMA_FILES[collection_name]
    # end if

    # Get model definition and properties
    model_def = models_definitions["definitions"][dataset_name][model_name]
    model_properties = model_def['properties']

    # Read CSV file
    df = pd.read_csv(
        os.path.join(dataset_root, dataset_name, collection_name + ".csv"),
        # parse_dates=['date', 'version'],
        # date_parser=custom_date_parser
    )

    # For each field
    for prop_name in list(df.columns):
        print("Prop. name: {}".format(prop_name))
        # Prop. description
        prop_desc = model_properties[prop_name]

        # Prop type
        if prop_desc['panda_type'] == 'datetime':
            # Transform to datetime
            df[prop_name] = pd.to_datetime(df[prop_name], format=prop_desc['format'])

            # Do we split in year, month, day?
            if 'split' in prop_desc and prop_desc['split']:
                split_datetime_field(df, prop_name)
            # end if
        elif prop_desc['panda_type'] == 'category':
            df[prop_name] = pd.Categorical(
                values=df[prop_name],
                categories=prop_desc['categories']
            )
        # end if
    # end for

    return df
# end load_dataset
