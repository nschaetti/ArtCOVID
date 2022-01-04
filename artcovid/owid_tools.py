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

# Imports local
from artcovid.data_retrieval import create_dataset_directory, download_file
from artcovid.constants import OWID_COVID19_CSV


# Download the OWID COVID19 dataset
def download_OWID_dataset(
        dest_dir: str
) -> None:
    r"""Download the OWID COVID19 dataset.

    :param dest_file:
    :return:
    """
    # OWID directory
    owid_dir = os.path.join(dest_dir, "owid")

    # Create if not exists
    create_dataset_directory(owid_dir)

    # Download CSV
    download_file(OWID_COVID19_CSV, os.path.join(owid_dir, "owid_dataset.csv"))
# end download_OWID_dataset

