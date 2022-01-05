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
from datetime import datetime
import re

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

# Load dataset
covid_df = load_dataset(
    "/home/schaetti/Projets/ZUCKER/YouTube/Artificialis Code/ArtCOVID/datasets/",
    "swissdata",
    "COVID19Cases_geoRegion"
)

print(covid_df)
print(covid_df.dtypes)
print(list(covid_df.columns))
# print(covid_df['datum'])
# print(pd.Categorical(values=covid_df['datum'].dt.month, categories=list(range(1, 13))))

# date_parser = lambda x: datetime.strptime(x, "%Y-%m-%d")
# version_date_parser = lambda x: datetime.strptime(x, "%Y-%m-%d_%H-%M-%S")
#
#
# # Custom date parser
# def custom_date_parser(
#         date_string: str
# ) -> datetime.date:
#     r"""Custom date parser.
#
#     :param date_string: Date as a string.
#     :return: Datetime
#     """
#     # Regex
#     version_date_format = r"^[0-9]+\-[0-9]+\-[0-9]+_[0-9]+\-[0-9]+\-[0-9]+$"
#     date_format = r"^[0-9]+\-[0-9]+\-[0-9]+$"
#
#     # Parse date
#     if len(re.findall(version_date_format, date_string)) == 1:
#         return datetime.strptime(date_string, "%Y-%m-%d_%H-%M-%S")
#     elif len(re.findall(date_format, date_string)) == 1:
#         return datetime.strptime(date_string, "%Y-%m-%d")
#     else:
#         raise ValueError("Unknown date format for \"{}\"".format(date_string))
#     # end if
# # end custom_date_parser
#
#
# df = pd.read_csv(
#     "/home/schaetti/Projets/ZUCKER/YouTube/Artificialis Code/ArtCOVID/datasets/swissdata/data/COVID19AdministeredDoses_vaccine.csv",
#     parse_dates=['date', 'version'],
#     date_parser=custom_date_parser
# )
#
# df['geoRegion'] = pd.Categorical(
#     values=df['geoRegion'],
#     categories=[
#         "AG",
#         "AI",
#         "AR",
#         "BE",
#         "BL",
#         "BS",
#         "CH",
#         "CHFL",
#         "FL",
#         "FR",
#         "GE",
#         "GL",
#         "GR",
#         "JU",
#         "LU",
#         "NE",
#         "NW",
#         "OW",
#         "SG",
#         "SH",
#         "SO",
#         "SZ",
#         "TG",
#         "TI",
#         "UR",
#         "VD",
#         "VS",
#         "ZG",
#         "ZH",
#         "all",
#         "neighboring_chfl",
#         "unknown"
#     ]
# )
#
# df['vaccine'] = pd.Categorical(
#     values=df['vaccine'],
#     categories=["johnson_johnson", "moderna", "pfizer_biontech"]
# )
#
# df['granularity'] = pd.Categorical(
#     values=df['granularity'],
#     categories=["detailed", "summary"]
# )
#
# print(df)
# print(df.dtypes)
# print(df.columns)
# print(df.ndim)
# print(df.shape)
# print(df['granularity'])
# print(df['granularity'].cat.codes)

