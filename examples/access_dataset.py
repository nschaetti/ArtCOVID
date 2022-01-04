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
import pandas as pd
import numpy as np

# Import ArtCOVID
from artcovid.dataset import load_dataset


# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo"
#     }
# )
#
# print(df2)
#
# s = pd.Series(["a", "b", "c", "a"], dtype="category")
# print(s)

load_dataset(
    "/home/schaetti/Projets/ZUCKER/YouTube/Artificialis Code/ArtCOVID/datasets/artcovid_dataset.h5",
    "swissdata",
    "COVID19AdministeredDoses_vaccine",
    "/home/schaetti/Projets/ZUCKER/YouTube/Artificialis Code/ArtCOVID/datasets/artcovid.schema.json"
)
