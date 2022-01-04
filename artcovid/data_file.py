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
import os
from typing import Tuple, Any, List, Dict
import h5py
import csv
import json

# Create H5 file for the dataset
from h5py import File, Dataset, Group


# Create H5 file
def create_h5_file(
    file_path: str
) -> tuple[File, Any, Any, Any]:
    r"""Create H5 file for the dataset

    :return:
    """
    # Open file
    h5_file = h5py.File(file_path, "w")

    # Create OWID dataset
    owid_group = h5_file.create_group("owid")

    # Create SwissData dataset
    swissdata_group = h5_file.create_group("swissdata")

    # Create data.gouv.fr dataset
    datagouvfr_group = h5_file.create_group("datagouvfr")

    return (
        h5_file,
        owid_group,
        swissdata_group,
        datagouvfr_group
    )
# end create_h5_file


# Read CSV
def read_csv(
        file_path: str
) -> tuple[Any, list[Any]]:
    r"""Read a CSV file.

    :param file_path:
    :return:
    """
    with open(file_path) as csv_file:
        # CSV reader
        csv_reader = csv.reader(csv_file)

        # List of rows
        rows_list = []

        # For each row
        for row_i, row in enumerate(csv_reader):
            if row_i == 0:
                header_row = row
            else:
                rows_list.append(row)
            # end if
        # end for
    # end with

    return header_row, rows_list
# end read_csv

