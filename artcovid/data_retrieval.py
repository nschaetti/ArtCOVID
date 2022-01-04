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
import requests
import os


# Create directory
def create_dataset_directory(
    directory_path: str
) -> None:
    r"""Create directory.

    :return:
    """
    # Create if not exists
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    # end if
# end create_dataset_directory


# Download file
def download_file(
        url_file: str,
        output_file: str
) -> None:
    r"""Download file from URL.

    :param url_file:
    :param output_file:
    :return:
    """
    # Download CSV
    with open(output_file, 'wb') as dest_file:
        # Request
        r = requests.get(url_file, allow_redirects=True)

        # Write
        dest_file.write(r.content)
    # end with
# end download_file


