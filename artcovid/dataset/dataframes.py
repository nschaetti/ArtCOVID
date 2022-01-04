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
import h5py
import pandas as pd
import json


# Load data
def load_dataset(
        h5_file: str,
        dataset_name: str,
        collection_name: str,
        models_defs_file: str
) -> pd.DataFrame:
    r"""Load data in the H5 file and return a Pandas DataFrame.

    :param h5_file: Path to the H5 file.
    :param dataset_name: Path in the H5 file to the dataset.
    :param models_defs_file: Path to the models definitions file.
    :return: A Pandas DataFrame.
    """
    # Open the H5 file
    with h5py.File(h5_file, 'r') as h5_fd, open(models_defs_file, 'r') as md_fd:
        # Load the dataset
        h5_dataset = h5_fd["{}/{}".format(dataset_name, collection_name)]

        # Load models definitions
        models_definitions = json.load(md_fd)

        # Get list of column names
        col_names = list(h5_dataset.dtype.fields.keys())

        # Get model definition
        model_definition = models_definitions["definitions"][dataset_name][collection_name]
        print(h5_dataset)
        print(h5_dataset.dtype)
        print(h5_dataset[0])
        print(col_names)
        print(model_definition)
    # end with
# end load_dataset
