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
import tempfile

import click
import requests
import urllib.request
import json
import os
import zipfile

# Imports local
from artcovid.data_file import create_h5_file
import artcovid.swissdata as sw
from artcovid.owid_tools import download_OWID_dataset
from artcovid.datagouvfr_tools import download_datagouvfr_dataset


# Main group of commands
@click.group('main')
def main():
    """
    Command line tools for the ArtCOVID project
    """
    pass
# end main


@main.command("download")
@click.option("--dataset-root", type=str, required=True, help="Path to the root destination directory of the dataset")
@click.option("--h5file", type=str, required=False, help="Path to the output H5 file")
@click.option("--models-definitions-file", type=str, required=True, help="Path to the models definitions JSON file (output)")
@click.option("--swissdata/--no-swissdata", default=True, help="Download data from SwissData")
@click.option("--owid/--no-owid", default=True, help="Download data from Our World In Data (OWID)")
@click.option("--datagouvfr/--no-datagouvfr", default=True, help="Download data from data.gouv.fr")
@click.option("--radiocanada/--no-radiocanada", default=True, help="Download data from Radio Canada")
def download(
        dataset_root: str,
        h5file: str,
        models_definitions_file: str,
        swissdata: bool,
        owid: bool,
        datagouvfr: bool,
        radiocanada: bool
):
    r"""Download the ArtCOVID dataset from various sources.

    :param dataset_root: Path to the root destination directory of the dataset
    :param models_definitions_file:
    :param h5file: Path to the output H5 file.
    :param swissdata: Download data from SwissData.
    :param owid: Download data from Our World In Data (OWID).
    :param datagouvfr: Download data from data.gouv.fr.
    :param radiocanada: Download data from radio-canada.
    """
    # Create H5 file
    if h5file is not None:
        h5_fd, owid_gr, swissdata_gr, datagouvfr_gr = create_h5_file(h5file)
    # end if

    # Create empty model definitions
    models_definitions = {
        '$id': "https://www.nilsschaetti.com/artcovid",
        'definitions': {}
    }

    # Download and convert swiss dataset
    if swissdata:
        # Log
        print("SwissData:")

        # Downloading SwissData dataset
        print("\tDownloading SwissData COVID dataset")
        sw.download_swissdata_dataset(dest_dir=dataset_root)

        # Update model definitions
        models_definitions = sw.extract_models_definitions(
            data_dir=dataset_root,
            models_definitions=models_definitions
        )

        # Convert the SwissData dataset to H5 file
        if h5file is not None:
            print("\tConverting the SwissData COVID dataset to H5 file")
            models_definitions = sw.swissdata_dataset_to_h5(
                data_dir=dataset_root,
                h5_group=swissdata_gr,
                models_definitions=models_definitions
            )
        # end if

        # Clean SwissData dataset
        sw.clean_dataset_directory(data_dir=dataset_root)
    # end if

    # Download the OWID COVID-19 dataset
    if owid:
        download_OWID_dataset(dest_dir=dataset_root)
    # end if

    # Download datagouvfr COVID-19 dataset
    if datagouvfr:
        download_datagouvfr_dataset(output_dir=dataset_root)
    # end if

    # Download Radio-Canada COVID-19 dataset
    if radiocanada:
        pass
    # end if

    # Save models definitions
    with open(models_definitions_file, 'w') as md_file:
        print("Saving models definitions at {}".format(models_definitions_file))
        json.dump(models_definitions, md_file, indent=True, sort_keys=True)
    # end with

    # Close file
    if h5file is not None:
        h5_fd.close()
    # end if
# end download


# Main
if __name__ == '__main__':
    main()
# end if



