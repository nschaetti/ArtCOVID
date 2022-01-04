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
from artcovid.constants import FRANCE_DATAGOUV_CSV
from artcovid.data_retrieval import create_dataset_directory, download_file


# Download data.gouv.fr dataset
def download_datagouvfr_dataset(
        output_dir: str
) -> None:
    r"""Download data.gouv.fr dataset.

    :param output_dir:
    :return:
    """
    # data.gouv.fr directory
    datagouvfr_dir = os.path.join(output_dir, "datagouvfr")

    # Create if not exists
    create_dataset_directory(datagouvfr_dir)

    # Download CSV
    download_file(FRANCE_DATAGOUV_CSV, os.path.join(datagouvfr_dir, "datagouvfr.csv"))
# end download_datagouvfr_datasaet

