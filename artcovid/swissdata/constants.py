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

##
##
## FILES
##
##

# region FILES

# Schema per file for Swiss Data
SWISSDATA_SCHEMA_FILES = {
    'COVID19Cases_geoRegion': 'DailyIncomingData',
    "COVID19Hosp_geoRegion": "DailyIncomingData",
    "COVID19Hosp_vaccpersons": "DailyHospVaccPersonsIncomingData",
    "COVID19Death_geoRegion": "DailyIncomingData",
    "COVID19Death_vaccpersons": "DailyDeathVaccPersonsIncomingData",
    "COVID19Test_geoRegion_all": "DailyIncomingData",
    "COVID19Test_geoRegion_PCR_Antigen": "DailyIncomingData",
    "COVID19Cases_geoRegion_w": "WeeklyIncomingData",
    "COVID19Hosp_geoRegion_w": "WeeklyIncomingData",
    "COVID19Death_geoRegion_w": "WeeklyIncomingData",
    "COVID19Test_geoRegion_w": "WeeklyIncomingData",
    "COVID19Test_geoRegion_PCR_Antigen_w": "WeeklyIncomingData",
    "COVID19Cases_geoRegion_AKL10_w": "WeeklyIncomingData",
    "COVID19Hosp_geoRegion_AKL10_w": "WeeklyIncomingData",
    "COVID19Hosp_vaccpersons_AKL10_w": "WeeklyHospVaccPersonsAgeRangeIncomingData",
    "COVID19Death_geoRegion_AKL10_w": "WeeklyIncomingData",
    "COVID19Death_vaccpersons_AKL10_w": "WeeklyDeathVaccPersonsAgeRangeIncomingData",
    "COVID19Test_geoRegion_AKL10_w": "WeeklyIncomingData",
    "COVID19Cases_geoRegion_sex_w": "WeeklyIncomingData",
    "COVID19Hosp_geoRegion_sex_w": "WeeklyIncomingData",
    "COVID19Hosp_vaccpersons_sex_w": "WeeklyHospVaccPersonsSexIncomingData",
    "COVID19Death_geoRegion_sex_w": "WeeklyIncomingData",
    "COVID19Death_vaccpersons_sex_w": "WeeklyDeathVaccPersonsSexIncomingData",
    "COVID19Test_geoRegion_sex_w": "WeeklyIncomingData",
    "COVID19WeeklyReportText": "WeeklyReportIncomingData",
    "COVID19Cases_extraGeoRegions_d": "AdditionalGeoRegionDailyIncomingData",
    "COVID19Cases_extraGeoRegions_14d":	"AdditionalGeoRegion14dPeriodIncomingData",
    "COVID19EvalTextDaily":	"DailyReportIncomingData",
    "COVID19QuarantineIsolation_geoRegion_d": "ContactTracingIncomingData",
    "COVID19HospCapacity_geoRegion": "HospCapacityDailyIncomingData",
    "COVID19IntQua": "InternationalQuarantineIncomingData",
    "COVID19IntCases": "InternationalDailyIncomingData",
    "COVID19Re_geoRegion": "ReDailyIncomingData",
    "COVID19VaccDosesDelivered": "VaccinationIncomingData",
    "COVID19VaccDosesDelivered_vaccine": "VaccinationDosesReceivedDeliveredVaccineIncomingData",
    "COVID19VaccDosesAdministered":	"VaccinationIncomingData",
    "COVID19AdministeredDoses_vaccine":	"VaccinationVaccineIncomingData",
    "COVID19VaccPersons_v2": "VaccPersonsIncomingData",
    "COVID19VaccPersons_vaccine": "VaccPersonsVaccineIncomingData",
    "COVID19VaccDosesAdministered_AKL10_w":	"VaccinationWeeklyIncomingData",
    "COVID19VaccPersons_AKL10_w_v2": "VaccPersonsWeeklyIncomingData",
    "COVID19VaccPersons_AKL10_vaccine_w": "VaccPersonsWeeklyAgeRangeVaccineIncomingData",
    "COVID19VaccDosesAdministered_sex_w": "VaccinationWeeklyIncomingData",
    "COVID19VaccPersons_sex_w_v2": "VaccPersonsWeeklyIncomingData",
    "COVID19FullyVaccPersons_indication_w_v2": "VaccPersonsWeeklyIndicationIncomingData",
    "COVID19VaccDosesAdministered_indication_w": "VaccinationWeeklyIndicationIncomingData",
    "COVID19VaccDosesAdministered_location_w": "VaccinationWeeklyLocationIncomingData",
    "COVID19VaccSymptoms": "VaccinationSymptomsIncomingData",
    "COVID19VaccDosesContingent": "VaccinationContingentIncomingData",
    "COVID19Variants_wgs": "VirusVariantsWgsDailyIncomingData",
    "COVID19Certificates": "CovidCertificatesDailyIncomingData"
}

# endregion FILES

##
##
## ENUMS
##
##

# region ENUMS

# Enum of geoRegion
SWISSDATA_GEOREGIONS_ENUM = [
    "AG",
    "AI",
    "AR",
    "BE",
    "BL",
    "BS",
    "CH",
    "CHFL",
    "FL",
    "FR",
    "GE",
    "GL",
    "GR",
    "JU",
    "LU",
    "NE",
    "NW",
    "OW",
    "SG",
    "SH",
    "SO",
    "SZ",
    "TG",
    "TI",
    "UR",
    "VD",
    "VS",
    "ZG",
    "ZH",
    "all",
    "neighboring_chfl"
]

# Enum for international GeoRegions
SWISSDATA_INT_GEOREGIONS_ENUM = [
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AT11",
    "AT12",
    "AT13",
    "AT21",
    "AT22",
    "AT31",
    "AT32",
    "AT33",
    "AT34",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DE1",
    "DE2",
    "DE3",
    "DE4",
    "DE5",
    "DE6",
    "DE7",
    "DE8",
    "DE9",
    "DEA",
    "DEB",
    "DEC",
    "DED",
    "DEE",
    "DEF",
    "DEG",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "FR1",
    "FRB",
    "FRC",
    "FRD",
    "FRE",
    "FRF",
    "FRG",
    "FRH",
    "FRI",
    "FRJ",
    "FRK",
    "FRL",
    "FRM",
    "FRY",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "ITC1",
    "ITC2",
    "ITC3",
    "ITC4",
    "ITF1",
    "ITF2",
    "ITF3",
    "ITF4",
    "ITF5",
    "ITF6",
    "ITG1",
    "ITG2",
    "ITH1",
    "ITH2",
    "ITH3",
    "ITH4",
    "ITH5",
    "ITI1",
    "ITI2",
    "ITI3",
    "ITI4",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WORLD",
    "WS",
    "XK",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW"
]

# Vaccine
SWISSDATA_VACCINE_ENUM = [
    "johnson_johnson",
    "moderna",
    "pfizer_biontech"
]

# Variant type
SWISSDATA_VACCINE_VARIANT_TYPE_ENUM = [
    "vaccine"
]

# Virus Variant WGS Type
SWISSDATA_VIRUS_VARIANT_WGS_TYPE_ENUM = [
    "B.1.1.318",
    "B.1.1.529",
    "B.1.1.7",
    "B.1.1.7 & E484K",
    "B.1.351",
    "B.1.525",
    "B.1.526",
    "B.1.617.1",
    "B.1.617.2",
    "C.37",
    "P.1",
    "P.2",
    "all_sequenced",
    "other_lineages"
]

# Granularity enum
SWISSDATA_GRANULARITY_ENUM = [
    "detailed",
    "summary"
]

# Nachweismethode enum
SWISSDATA_NACHWEISMETHODE_ENUM = [
    "Antigen_Schnelltest",
    "PCR",
    "all"
]

# Datum Unit
SWISSDATA_DATUM_UNIT_ENUM = [
    "isoweek",
    "day"
]

# Types
SWISSDATA_TYPE_ENUM = [
    "COVID19Cases"
]

# Data completeness
SWISSDATA_COMPLETENESS_ENUM = [
    "complete",
    "high",
    "intermediate",
    "limited"
]

# Weekly report enum
SWISSDATA_WEEKLY_REPORT_ENUM = [
    "COVID19weeklyReportText"
]

# Incoming Epidemiologic Vaccination Status Schema
SWISSDATA_VACCINATION_STATUS_ENUM = [
    "fully_vaccinated",
    "not_vaccinated",
    "partially_vaccinated",
    "unknown"
]

# Classification enum
SWISSDATA_CLASSIFICATION_ENUM = [
    "default"
]

# Data source enum
SWISSDATA_SOURCE_ENUM = [
    "msys",
    "wgs",
    "BAG",
    "OWID",
    "WHO"
]

# Sex enum
SWISSDATA_SEX_ENUM = [
    "female",
    "male",
    "unknown"
]

# Age range
SWISSDATA_INCOMING_AGE_RANGE_ENUM = [
    "0 - 9",
    "10 - 19",
    "20 - 29",
    "30 - 39",
    "40 - 49",
    "50 - 59",
    "60 - 69",
    "70 - 79",
    "80+"
]

# Vaccination Symptoms Age Range
SWISSDATA_VACCINATION_AGE_RANGE_ENUM = [
    "0 - 1",
    "12 - 17",
    "18 - 44",
    "2 - 11",
    "45 - 64",
    "65 - 74",
    "75+",
    "all",
    "unknown"
]

# Incidence Category Normalized enum
SWISSDATA_INZ_CATEGORY_NORMALIZED_ENUM = [
    "0-59",
    "120-239",
    "1920+",
    "240-479",
    "480-959",
    "60-119",
    "960-1919",
]

# Geo-Region Type Enum
SWISSDATA_GEOREGION_TYPE_ENUM = [
    "CH",
    "GBAE",
    "GR",
    "KTN"
]

# Geo-Level Enum
SWISSDATA_INT_GEOLEVEL_ENUM = [
    "ISO2",
    "NUTS-1",
    "NUTS-2",
]

# Age Group Type enum
SWISSDATA_AGE_GROUP_TYPE_ENUM = [
    "age_group_AKL10",
    "age_group_vacc_strategy"
]

# Vaccinated Persons Age Group Enum
SWISSDATA_VACC_PERSONS_AGE_GROUP_ENUM = [
    "12+",
    "total_population"
]

# Indication enum
SWISSDATA_INDICATION_ENUM = [
    "age",
    "all",
    "chronic_disease",
    "contact_comm",
    "contact_vuln",
    "med_prof",
    "not_vaccinated",
    "other",
    "risk_groups",
]

# Vaccinated Person enum
SWISSDATA_VACC_PERSONS_ENUM = [
    "COVID19AtLeastOneDosePersons",
    "COVID19FirstBoosterPersons",
    "COVID19FullyVaccPersons",
    "COVID19PartiallyVaccPersons",
    "COVID19VaccDosesAdministered"
]

# Location
SWISSDATA_LOCATION_ENUM = [
    "hospital",
    "medical_practice",
    "nursing_home",
    "other",
    "pharmacy",
    "vaccination_centre"
]

# Severity
SWISSDATA_SEVERITY_ENUM = [
    "all",
    "not_serious",
    "serious"
]

# endregion ENUMS

##
##
## FIELDS DESCRIPTION
##
##

# region FIELDS

# Data field (YYYY-MM-DD)
SWISSDATA_DATE_YYYYMMDD_FIELD = {
    "ptype": "date",
    "panda_type": "datetime",
    "format": "%Y-%m-%d",
    "regex": "[0-9]{4}\-[0-9]{2}\-[0-9]{2}",
    "split": True,
    "optional": True,
    "null": False
}

# Datetime field (YYYY-MM-DD_HH-mm-SS)
SWISSDATA_DATETIME_FIELD = {
    "ptype": "datetime",
    "panda_type": "datetime",
    "format": "%Y-%m-%d_%H-%M-%S",
    "regex": "[0-9]{4}\-[0-9]{2}\-[0-9]{2}_[0-9]{2}\-[0-9]{2}\-[0-9]{2}",
    "optional": True,
    "null": False
}

# Version field
SWISSDATA_VERSION_FIELD = SWISSDATA_DATETIME_FIELD

# Float field
SWISSDATA_FLOAT_FIELD = {
    "ptype": "f",
    "panda_type": "float64",
    "optional": True,
    "null": False
}

# Integer field
SWISSDATA_INTEGER_FIELD = {
    "ptype": "f",
    "panda_type": "int64",
    "optional": True,
    "null": False
}

# Boolean field
SWISSDATA_BOOLEAN_FIELD = {
    "ptype": "b",
    "panda_type": "bool",
    "optional": True,
    "null": False
}

# String field
SWISSDATA_STRING_FIELD = {
    "ptype": "s",
    "panda_type": "object",
    "optional": True,
    "null": False
}

# ISO-Week field
SWISSDATA_DATE_ISOWEEK_FIELD = {
    "ptype": "i",
    "panda_type": "isoweek-int",
    "optional": True,
    "null": False
}

# ISO-Week string field
SWISSDATA_DATE_ISOWEEK_STR_FIELD = {
    "ptype": "s",
    "panda_type": "isoweek-str",
    "format": "YYYY-MM",
    "regex": "[0-9]{4}\-[0-9]{2}",
    "optional": True,
    "null": False
}

# GeoRegion
SWISSDATA_GEOREGIONS_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_GEOREGIONS_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_GEOREGIONS_ENUM,
    "optional": True,
    "null": False
}

# International GeoRegion
SWISSDATA_INT_GEOREGIONS_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_INT_GEOREGIONS_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_INT_GEOREGIONS_ENUM,
    "optional": True,
    "null": False
}

# Variant Type
SWISSDATA_VARIANT_TYPE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VIRUS_VARIANT_WGS_TYPE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VIRUS_VARIANT_WGS_TYPE_ENUM,
    "optional": True,
    "null": False
}

# Vaccination Status
SWISSDATA_VACCINATION_STATUS_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACCINATION_STATUS_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACCINATION_STATUS_ENUM,
    "optional": True,
    "null": False
}

# Vaccine field
SWISSDATA_VACCINE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACCINE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACCINE_ENUM,
    "optional": True,
    "null": False
}

# Classification field
SWISSDATA_CLASSIFICATION_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_CLASSIFICATION_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_CLASSIFICATION_ENUM,
    "optional": True,
    "null": False
}

# Data completeness field
SWISSDATA_COMPLETENESS_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_COMPLETENESS_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_COMPLETENESS_ENUM,
    "optional": True,
    "null": False
}

# Data source field
SWISSDATA_SOURCE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_SOURCE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_SOURCE_ENUM,
    "optional": True,
    "null": False
}

# Vaccine Variant Type
SWISSDATA_VACCINE_VARIANT_TYPE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACCINE_VARIANT_TYPE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACCINE_VARIANT_TYPE_ENUM,
    "optional": True,
    "null": False
}

# Granularity
SWISSDATA_GRANULARITY_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_GRANULARITY_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_GRANULARITY_ENUM,
    "optional": True,
    "null": False
}

# Datum Unit
SWISSDATA_DATUM_UNIT_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_DATUM_UNIT_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_DATUM_UNIT_ENUM,
    "optional": True,
    "null": False
}

# NACHWEIS METHODE
SWISSDATA_NACHWEISMETHODE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_NACHWEISMETHODE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_NACHWEISMETHODE_ENUM,
    "optional": True,
    "null": False
}

# Sex
SWISSDATA_SEX_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_SEX_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_SEX_ENUM,
    "optional": True,
    "null": False
}

# Incoming Age Range
SWISSDATA_INCOMING_AGE_RANGE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_INCOMING_AGE_RANGE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_INCOMING_AGE_RANGE_ENUM,
    "optional": True,
    "null": False
}

# Inz Category Normalized
SWISSDATA_INZ_CATEGORY_NORMALIZED_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_INZ_CATEGORY_NORMALIZED_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_INZ_CATEGORY_NORMALIZED_ENUM,
    "optional": True,
    "null": False
}

# Geo-Region Type
SWISSDATA_GEOREGION_TYPE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_GEOREGION_TYPE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_GEOREGION_TYPE_ENUM,
    "optional": True,
    "null": False
}

# Geo-Level
SWISSDATA_INT_GEOLEVEL_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_INT_GEOLEVEL_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_INT_GEOLEVEL_ENUM,
    "optional": True,
    "null": False
}

# Age Group Type
SWISSDATA_AGE_GROUP_TYPE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_AGE_GROUP_TYPE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_AGE_GROUP_TYPE_ENUM,
    "optional": True,
    "null": False
}

# Vaccinated Persons Age Group
SWISSDATA_VACC_PERSONS_AGE_GROUP_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACC_PERSONS_AGE_GROUP_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACC_PERSONS_AGE_GROUP_ENUM,
    "optional": True,
    "null": False
}

# Indication
SWISSDATA_INDICATION_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_INDICATION_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_INDICATION_ENUM,
    "optional": True,
    "null": False
}

# Vacc. Persons
SWISSDATA_VACC_PERSONS_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACC_PERSONS_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACC_PERSONS_ENUM,
    "optional": True,
    "null": False
}

# Location
SWISSDATA_LOCATION_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_LOCATION_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_LOCATION_ENUM,
    "optional": True,
    "null": False
}

# Vaccination Symptoms Age Range
SWISSDATA_VACCINATION_AGE_RANGE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_VACCINATION_AGE_RANGE_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_VACCINATION_AGE_RANGE_ENUM,
    "optional": True,
    "null": False
}

# Severity
SWISSDATA_SEVERITY_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {**{k: k_i for k_i, k in enumerate(SWISSDATA_SEVERITY_ENUM)}, **{'na': -1}},
    "categories": SWISSDATA_SEVERITY_ENUM,
    "optional": True,
    "null": False
}

# Type-variant vaccine
SWISSDATA_TYPE_VARIANT_VACCINE_FIELD = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {
        "na": -1,
        "vaccine": 0
    },
    "categories": [
        "vaccine"
    ],
    "optional": True,
    "null": False
}

# Type-variant age-sex
SWISSDATA_TYPE_VARIANT_AGE_SEX = {
    "ptype": "enum",
    "panda_type": "category",
    "values": {
        "na": -1,
        "altersklasse_covid19": 0,
        "sex": 1
    },
    "categories": [
        "altersklasse_covid19",
        "sex"
    ],
    "optional": True,
    "null": False,
}

# endregion FIELDS

##
##
## PROPERTIES
##
##

# region PROPERTIES

# Vaccination vaccine incoming data properties
SWISSDATA_VACCINATION_VACCINE_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "per100Persons_mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_STRING_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Daily Incoming Data Properties
SWISSDATA_DAILY_INCOMING_DATA_PROPERTIES = {
    "anteil_pos_14": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_28": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_all": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_phase2": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_phase2b": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_phase3": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_phase4": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_phase5": SWISSDATA_FLOAT_FIELD,
    "datum": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "datum_unit": SWISSDATA_DATUM_UNIT_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "entries_diff_last": SWISSDATA_INTEGER_FIELD,
    "entries_diff_last_age": SWISSDATA_INTEGER_FIELD,
    "entries_letzter_stand": SWISSDATA_INTEGER_FIELD,
    "entries_neg": SWISSDATA_INTEGER_FIELD,
    "entries_neu_gemeldet": SWISSDATA_INTEGER_FIELD,
    "entries_pos": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzdelta7d": SWISSDATA_FLOAT_FIELD,
    "inzmean7d": SWISSDATA_FLOAT_FIELD,
    "inzmean14d": SWISSDATA_FLOAT_FIELD,
    "inzsum14d": SWISSDATA_FLOAT_FIELD,
    "inzsum7d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_Phase2": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_Phase2b": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_Phase3": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_Phase4": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_Phase5": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_last14d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_last28d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal_last7d": SWISSDATA_FLOAT_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "mean14d": SWISSDATA_FLOAT_FIELD,
    "nachweismethode": SWISSDATA_NACHWEISMETHODE_FIELD,
    "offset_Phase2": SWISSDATA_INTEGER_FIELD,
    "offset_Phase2b": SWISSDATA_INTEGER_FIELD,
    "offset_Phase3": SWISSDATA_INTEGER_FIELD,
    "offset_Phase4": SWISSDATA_INTEGER_FIELD,
    "offset_Phase5": SWISSDATA_INTEGER_FIELD,
    "offset_last14d": SWISSDATA_INTEGER_FIELD,
    "offset_last28d": SWISSDATA_INTEGER_FIELD,
    "offset_last7d": SWISSDATA_INTEGER_FIELD,
    "offset_vacc_info": SWISSDATA_INTEGER_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "pos_anteil": SWISSDATA_FLOAT_FIELD,
    "pos_anteil_mean7d": SWISSDATA_FLOAT_FIELD,
    "sum14d": SWISSDATA_INTEGER_FIELD,
    "sum7d": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "sumTotal_Phase2": SWISSDATA_INTEGER_FIELD,
    "sumTotal_Phase2b": SWISSDATA_INTEGER_FIELD,
    "sumTotal_Phase3": SWISSDATA_INTEGER_FIELD,
    "sumTotal_Phase4": SWISSDATA_INTEGER_FIELD,
    "sumTotal_Phase5": SWISSDATA_INTEGER_FIELD,
    "sumTotal_last14d": SWISSDATA_INTEGER_FIELD,
    "sumTotal_last28d": SWISSDATA_INTEGER_FIELD,
    "sumTotal_last7d": SWISSDATA_INTEGER_FIELD,
    "sumTotal_vacc_info": SWISSDATA_INTEGER_FIELD,
    "sumdelta7d": SWISSDATA_INTEGER_FIELD,
    "timeframe_14d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_28d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_7d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2b": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase3": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase4": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase5": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_vacc_info": SWISSDATA_BOOLEAN_FIELD,
    "type": SWISSDATA_STRING_FIELD,
        "type_variant": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
        },
        "categories": [
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}


# Weekly Report Incoming Data Properties
SWISSDATA_WEEKLY_REPORT_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_ISOWEEK_FIELD,
    "de": SWISSDATA_STRING_FIELD,
    "en": SWISSDATA_STRING_FIELD,
    "fr": SWISSDATA_STRING_FIELD,
    "identifier": SWISSDATA_STRING_FIELD,
    "it": SWISSDATA_STRING_FIELD,
    "rm": SWISSDATA_STRING_FIELD,
    "type": SWISSDATA_STRING_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}


# Virus Variants WGS Daily Incoming Data Properties
SWISSDATA_VIRUS_VARIANTS_WGS_DAILY_INCOMING_DATA_PROPERTIES = {
    "classification": SWISSDATA_CLASSIFICATION_FIELD,
    "data_source": SWISSDATA_SOURCE_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prct_lower_ci": SWISSDATA_FLOAT_FIELD,
    "prct_mean7d": SWISSDATA_FLOAT_FIELD,
    "prct_upper_ci": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "type": SWISSDATA_STRING_FIELD,
    "variant_type": SWISSDATA_VARIANT_TYPE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Hospitalisation Vaccine Persons Incoming Data
SWISSDATA_HOSP_VACC_PERSONS_INCOMING_DATA_PROPERTIES = {
    "data_completeness": SWISSDATA_COMPLETENESS_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzmean7d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prctSumTotal": SWISSDATA_FLOAT_FIELD,
    "prct_mean7d": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_STRING_FIELD,
    "type_variant": SWISSDATA_VACCINE_VARIANT_TYPE_FIELD,
    "vaccination_status": SWISSDATA_VACCINATION_STATUS_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Weekly Incoming Data
SWISSDATA_WEEKLY_INCOMING_DATA_PROPERTIES = {
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "anteil_pos": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_all": SWISSDATA_FLOAT_FIELD,
    "anteil_pos_diff": SWISSDATA_FLOAT_FIELD,
    "datum": SWISSDATA_DATE_ISOWEEK_FIELD,
    "datum_dboardformated": SWISSDATA_DATE_ISOWEEK_STR_FIELD,
    "datum_unit": SWISSDATA_DATUM_UNIT_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "entries_pos": SWISSDATA_INTEGER_FIELD,
    "entries_neg": SWISSDATA_INTEGER_FIELD,
    "entries_diff_abs": SWISSDATA_INTEGER_FIELD,
    "entries_diff_inz": SWISSDATA_FLOAT_FIELD,
    "entries_diff_pct": SWISSDATA_FLOAT_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "nachweismethode": SWISSDATA_NACHWEISMETHODE_FIELD,
    "offset_vacc_info": SWISSDATA_INTEGER_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prct_diff": SWISSDATA_FLOAT_FIELD,
    "sex": SWISSDATA_SEX_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "sumTotal_vacc_info": SWISSDATA_INTEGER_FIELD,
    "timeframe_14d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_28d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_7d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2b": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase3": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase4": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase5": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_vacc_info": SWISSDATA_BOOLEAN_FIELD,
    "type": SWISSDATA_STRING_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_AGE_SEX,
    "version": SWISSDATA_VERSION_FIELD
}

# Daily Death Vacc Persones Incoming Data Properties
SWISSDATA_DAILY_DEATH_VACC_PERSONS_INCOMING_DATA_PROPERTIES = {
    "data_completeness": SWISSDATA_COMPLETENESS_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzmean7d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prctSumTotal": SWISSDATA_FLOAT_FIELD,
    "prct_mean7d": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "COVID19Death": 0
        },
        "categories": [
            "COVID19Death"
        ],
        "optional": True,
        "null": False,
    },
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccination_status": SWISSDATA_VACCINATION_STATUS_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Weekly Hospitalisation Vaccined Persons Age Range Incoming Data Properties
SWISSDATA_WEEKLY_HOSP_VACC_PERSONS_AGE_RANGE_INCOMING_DATA_PROPERTIES = {
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "data_completeness": SWISSDATA_COMPLETENESS_FIELD,
    "date": SWISSDATA_DATE_ISOWEEK_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "COVID19Hosp": 0
        },
        "categories": [
            "COVID19Hosp"
        ],
        "optional": True,
        "null": False,
    },
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccination_status": SWISSDATA_VACCINATION_STATUS_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Weekly Death Vaccinated Persons Age Range Incoming Data Properties
SWISSDATA_WEEKLY_DEATH_VACC_PERSONS_AGE_RANGE_INCOMING_DATA_PROPERTIES = {
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "data_completeness": SWISSDATA_COMPLETENESS_FIELD,
    "date": SWISSDATA_DATE_ISOWEEK_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Death": 1
        },
        "categories": [
            "COVID19Death"
        ],
        "optional": True,
        "null": False,
    },
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccination_status": SWISSDATA_VACCINATION_STATUS_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Weekly Hospitalisation Vaccined Persons Sex Incoming Data Properties
SWISSDATA_WEEKLY_HOSP_VACC_PERSONS_SEX_INCOMING_DATA_PROPERTIES = {
    "data_completeness": SWISSDATA_COMPLETENESS_FIELD,
    "date": SWISSDATA_DATE_ISOWEEK_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sex": SWISSDATA_SEX_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Hosp": 1
        },
        "categories": [
            "COVID19Hosp"
        ],
        "optional": True,
        "null": False,
    },
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccination_status": SWISSDATA_VACCINATION_STATUS_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Additional Geo-Region Daily Incoming Data Properties
SWISSDATA_ADDITIONAL_GEO_REGION_DAILY_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "geoRegion_type": SWISSDATA_GEOREGION_TYPE_FIELD,
    "geoVersion": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "inzCategoryNormalized": SWISSDATA_INZ_CATEGORY_NORMALIZED_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Cases": 1
        },
        "categories": [
            "COVID19Cases"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Additional Geo-Region 14 days Period Incoming Data Properties
SWISSDATA_ADDITIONAL_GEO_REGION_14D_PERIOD_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "geoRegion_type": SWISSDATA_GEOREGION_TYPE_FIELD,
    "geoVersion": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "inzCategoryNormalized": SWISSDATA_INZ_CATEGORY_NORMALIZED_FIELD,
    "period_end_date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "period_start_date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Cases": 1
        },
        "categories": [
            "COVID19Cases"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Daily Report Incoming Data Properties
SWISSDATA_DAILY_REPORT_INCOMING_DATA_PROPERTIES = {
    "content.de": SWISSDATA_STRING_FIELD,
    "content.en": SWISSDATA_STRING_FIELD,
    "content.fr": SWISSDATA_STRING_FIELD,
    "content.it": SWISSDATA_STRING_FIELD,
    "content.rm": SWISSDATA_STRING_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19EvalTextDaily": 1
        },
        "categories": [
            "COVID19EvalTextDaily"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Contact Tracing Incoming Data
SWISSDATA_CONTACT_TRACING_INCOMING_DATA_PROPERTIES = {
    "date_unit": SWISSDATA_DATUM_UNIT_FIELD,
    "datum": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19CT_Entry": 1,
            "COVID19CT_Iso": 2,
            "COVID19CT_Qua": 3,
            "COVID19CT_reporting_cantons": 4
        },
        "categories": [
            "COVID19CT_Entry",
            "COVID19CT_Iso",
            "COVID19CT_Qua",
            "COVID19CT_reporting_cantons"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Hospital Capacity Daily Incoming Data Properties
SWISSDATA_HOSP_CAPACITY_DAILY_INCOMING_DATA_PROPERTIES = {
    "ICUPercent_AllPatients": SWISSDATA_FLOAT_FIELD,
    "ICUPercent_Capacity": SWISSDATA_FLOAT_FIELD,
    "ICUPercent_Covid19Patients": SWISSDATA_FLOAT_FIELD,
    "ICUPercent_FreeCapacity": SWISSDATA_FLOAT_FIELD,
    "ICUPercent_NonCovid19Patients": SWISSDATA_FLOAT_FIELD,
    "ICU_AllPatients": SWISSDATA_INTEGER_FIELD,
    "ICU_AllPatients_mean15d": SWISSDATA_FLOAT_FIELD,
    "ICU_Capacity": SWISSDATA_INTEGER_FIELD,
    "ICU_Capacity_mean15d": SWISSDATA_FLOAT_FIELD,
    "ICU_Covid19Patients": SWISSDATA_INTEGER_FIELD,
    "ICU_Covid19Patients_mean15d": SWISSDATA_FLOAT_FIELD,
    "ICU_FreeCapacity": SWISSDATA_INTEGER_FIELD,
    "ICU_FreeCapacity_mean15d": SWISSDATA_FLOAT_FIELD,
    "ICU_NonCovid19Patients": SWISSDATA_INTEGER_FIELD,
    "ICU_NonCovid19Patients_mean15d": SWISSDATA_FLOAT_FIELD,
    "ICU_exists": SWISSDATA_BOOLEAN_FIELD,
    "TotalPercent_AllPatients": SWISSDATA_FLOAT_FIELD,
    "TotalPercent_Capacity": SWISSDATA_INTEGER_FIELD,
    "TotalPercent_Covid19Patients": SWISSDATA_FLOAT_FIELD,
    "TotalPercent_FreeCapacity": SWISSDATA_FLOAT_FIELD,
    "TotalPercent_NonCovid19Patients": SWISSDATA_FLOAT_FIELD,
    "Total_AllPatients": SWISSDATA_INTEGER_FIELD,
    "Total_AllPatients_mean15d": SWISSDATA_FLOAT_FIELD,
    "Total_Capacity": SWISSDATA_INTEGER_FIELD,
    "Total_Capacity_mean15d": SWISSDATA_FLOAT_FIELD,
    "Total_Covid19Patients": SWISSDATA_INTEGER_FIELD,
    "Total_Covid19Patients_mean15d": SWISSDATA_FLOAT_FIELD,
    "Total_FreeCapacity": SWISSDATA_INTEGER_FIELD,
    "Total_FreeCapacity_mean15d": SWISSDATA_FLOAT_FIELD,
    "Total_NonCovid19Patients": SWISSDATA_INTEGER_FIELD,
    "Total_NonCovid19Patients_mean15d": SWISSDATA_FLOAT_FIELD,
    "Total_exists": SWISSDATA_BOOLEAN_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "timeframe_14d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_28d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_7d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2b": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase3": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase4": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase5": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_vacc_info": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19HospCapacity": 1
        },
        "optional": True,
        "null": False,
    },
    "type_variant": {
        "title": "type_variant",
        "type": "string",
        "panda_type": "category",
        "ptype": "enum",
        "values": {
            "na": -1,
            "fp7d": 1,
            "nfp": 2
        },
        "categories": [
            "fp7d",
            "nfp"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# International Quarantine Incoming Data Properties
SWISSDATA_INTERNATIONAL_QUARANTINE_INCOMING_DATA_PROPERTIES = {
    "geoLevel": SWISSDATA_INT_GEOLEVEL_FIELD,
    "geoRegion": SWISSDATA_INT_GEOREGIONS_FIELD,
    "quarantineEnd": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "quarantineStart": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19IntQua": 1
        },
        "categories": [
            "COVID19IntQua"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# International Daily Incoming Data Properties
SWISSDATA_INTERNATIONAL_DAILY_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoLevel": SWISSDATA_INT_GEOLEVEL_FIELD,
    "geoRegion": SWISSDATA_INT_GEOREGIONS_FIELD,
    "geoRegionName": SWISSDATA_STRING_FIELD,
    "inz_entries": SWISSDATA_FLOAT_FIELD,
    "inzsum14d": SWISSDATA_FLOAT_FIELD,
    "inzsumTotal": SWISSDATA_FLOAT_FIELD,
    "population": SWISSDATA_INTEGER_FIELD,
    "source": SWISSDATA_SOURCE_FIELD,
    "sum14d": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "timeframe_14d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_28d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2b": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase3": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase4": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase5": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "COVID19IntCases": 1
        },
        "categories": [
            "COVID19IntCases"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# ReDaily Incoming Data Properties
SWISSDATA_REDAILY_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "median_R_highHPD": SWISSDATA_FLOAT_FIELD,
    "median_R_lowHPD": SWISSDATA_FLOAT_FIELD,
    "median_R_mean": SWISSDATA_FLOAT_FIELD,
    "median_R_mean_mean7d": SWISSDATA_FLOAT_FIELD,
    "timeframe_14d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_28d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_7d": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_all": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase2b": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase3": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase4": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_phase5": SWISSDATA_BOOLEAN_FIELD,
    "timeframe_vacc_info": SWISSDATA_BOOLEAN_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Cases": 1,
            "COVID19Death": 2,
            "COVID19Hosp": 3,
            "COVID19HospCapacity": 4,
            "COVID19Re": 5,
            "COVID19Test": 6,
        },
        "categories": [
            "COVID19Cases",
            "COVID19Death",
            "COVID19Hosp",
            "COVID19HospCapacity",
            "COVID19Re",
            "COVID19Test"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Incoming Data Properties
SWISSDATA_VACCINATION_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "per100Persons_mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19AtLeastOneDosePersons": 1,
            "COVID19FirstBoosterPersons": 2,
            "COVID19FullyVaccPersons": 3,
            "COVID19NotVaccPersons": 4,
            "COVID19PartiallyVaccPersons": 5,
            "COVID19VaccDosesAdministered": 6,
            "COVID19VaccDosesDelivered": 7,
            "COVID19VaccDosesReceived": 8
        },
        "categories": [
            "COVID19AtLeastOneDosePersons",
            "COVID19FirstBoosterPersons",
            "COVID19FullyVaccPersons",
            "COVID19NotVaccPersons",
            "COVID19PartiallyVaccPersons",
            "COVID19VaccDosesAdministered",
            "COVID19VaccDosesDelivered",
            "COVID19VaccDosesReceived"
        ],
        "optional": True,
        "null": False,
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Doses Received Delivered Vaccine Incoming Data Properties
SWISSDATA_VACCINATION_DOSES_RECEIVED_DELIVERED_VACCINE_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19VaccDosesDelivered": 1,
            "COVID19VaccDosesReceived": 2
        },
        "optional": True,
        "null": False,
    },
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Persons Incoming Data Properties
SWISSDATA_VACC_PERSONS_INCOMING_DATA_PROPERTIES = {
    "age_group": SWISSDATA_VACC_PERSONS_AGE_GROUP_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "per100Persons_mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccined Persons Vaccine Incoming Data Properties
SWISSDATA_VACC_PERSONS_VACCINE_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "mean7d": SWISSDATA_FLOAT_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "per100Persons_mean7d": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_VACCINE_FIELD,
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Weekly Incoming Data Properties
SWISSDATA_VACCINATION_WEEKLY_INCOMING_DATA_PROPERTIES = {
    "age_group_type": SWISSDATA_AGE_GROUP_TYPE_FIELD,
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "sex": SWISSDATA_SEX_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_AGE_SEX,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Persons Weekly Incoming Data Properties
SWISSDATA_VACC_PERSONS_WEEKLY_INCOMING_DATA_PROPERTIES = {
    "age_group_type": SWISSDATA_AGE_GROUP_TYPE_FIELD,
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "sex": SWISSDATA_SEX_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_AGE_SEX,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccined Persons Weekly Indication Incoming Data
SWISSDATA_VACC_PERSONS_WEEKLY_INDICATION_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "indication": SWISSDATA_INDICATION_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prctPop": SWISSDATA_FLOAT_FIELD,
    "prctPopSumTotal": SWISSDATA_FLOAT_FIELD,
    "prctSumTotal": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "indication": 1
        },
        "categories": [
            "indication"
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Vacc. Persons Weekly Age Range Vacine Incoming Data Properties
SWISSDATA_VACC_PERSONS_WEEKLY_AGE_RANGE_VACCINE_INCOMING_DATA_PROPERTIES = {
    "altersklasse_covid19": SWISSDATA_INCOMING_AGE_RANGE_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": SWISSDATA_TYPE_VARIANT_AGE_SEX,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Weekly Indication Incoming Data Properties
SWISSDATA_VACCINATION_WEEKLY_INDICATION_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "indication": SWISSDATA_INDICATION_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prctPop": SWISSDATA_FLOAT_FIELD,
    "prctPopSumTotal": SWISSDATA_FLOAT_FIELD,
    "prctSumTotal": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "indication": 1
        },
        "categories": [
            "indication"
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Weekly Location Incoming Data Properties
SWISSDATA_VACCINATION_WEEKLY_LOCATION_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "freq": SWISSDATA_FLOAT_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "granularity": SWISSDATA_GRANULARITY_FIELD,
    "location": SWISSDATA_LOCATION_FIELD,
    "per100Persons": SWISSDATA_FLOAT_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "prct": SWISSDATA_FLOAT_FIELD,
    "prctSumTotal": SWISSDATA_FLOAT_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": SWISSDATA_VACC_PERSONS_FIELD,
    "type_variant": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "location": 1
        },
        "categories": [
          "location"
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Symptoms Incoming Data Properties
SWISSDATA_VACCINATION_SYMPTOMS_INCOMING_DATA_PROPERTIES = {
    "age_group": SWISSDATA_VACCINATION_AGE_RANGE_FIELD,
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "severity": SWISSDATA_SEVERITY_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19VaccSymptoms": 1
        },
        "categories": [
          "COVID19VaccSymptoms"
        ],
        "optional": True,
        "null": False
    },
    "vaccine": SWISSDATA_VACCINE_FIELD,
    "version": SWISSDATA_VERSION_FIELD
}

# Vaccination Contingent Incoming Data Properties
SWISSDATA_VACCINATION_CONTINGENT_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "per100PersonsTotal": SWISSDATA_FLOAT_FIELD,
    "pop": SWISSDATA_INTEGER_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19VaccDosesContingent": 1
        },
        "categories": [
          "COVID19VaccDosesContingent"
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}

# COVID-19 Certificate Daily Incoming Data Properties
SWISSDATA_COVID_CERTIFICATE_DAILY_INCOMING_DATA_PROPERTIES = {
    "date": SWISSDATA_DATE_YYYYMMDD_FIELD,
    "entries": SWISSDATA_INTEGER_FIELD,
    "geoRegion": SWISSDATA_GEOREGIONS_FIELD,
    "sumTotal": SWISSDATA_INTEGER_FIELD,
    "type": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "COVID19Certificates": 1
        },
        "categories": [
          "COVID19Certificates"
        ],
        "optional": True,
        "null": False
    },
    "type_variant": {
        "ptype": "enum",
        "panda_type": "category",
        "values": {
            "na": -1,
            "none": 0,
            "all": 1,
            "recovered": 2,
            "tested": 3,
            "vaccinated": 4,
        },
        "categories": [
            "all",
            "recovered",
            "tested",
            "vaccinated"
        ],
        "optional": True,
        "null": False
    },
    "version": SWISSDATA_VERSION_FIELD
}

# endregion PROPERTIES

##
##
## DATA DESCRIPTION
##
##

# region DATA

# All data descriptions
SWISSDATA_DATA_DESCRIPTION = {
    "VaccinationVaccineIncomingData": {
        "properties": SWISSDATA_VACCINATION_VACCINE_INCOMING_DATA_PROPERTIES
    },
    "DailyIncomingData": {
        "properties": SWISSDATA_DAILY_INCOMING_DATA_PROPERTIES
    },
    "WeeklyReportIncomingData": {
        "properties": SWISSDATA_WEEKLY_REPORT_INCOMING_DATA_PROPERTIES
    },
    "VirusVariantsWgsDailyIncomingData": {
        "properties": SWISSDATA_VIRUS_VARIANTS_WGS_DAILY_INCOMING_DATA_PROPERTIES
    },
    "DailyHospVaccPersonsIncomingData": {
        "properties": SWISSDATA_HOSP_VACC_PERSONS_INCOMING_DATA_PROPERTIES
    },
    "WeeklyIncomingData": {
        "properties": SWISSDATA_WEEKLY_INCOMING_DATA_PROPERTIES
    },
    "DailyDeathVaccPersonsIncomingData": {
        "properties": SWISSDATA_DAILY_DEATH_VACC_PERSONS_INCOMING_DATA_PROPERTIES
    },
    "WeeklyHospVaccPersonsAgeRangeIncomingData": {
        "properties": SWISSDATA_WEEKLY_HOSP_VACC_PERSONS_AGE_RANGE_INCOMING_DATA_PROPERTIES
    },
    "WeeklyDeathVaccPersonsAgeRangeIncomingData": {
        "properties": SWISSDATA_WEEKLY_DEATH_VACC_PERSONS_AGE_RANGE_INCOMING_DATA_PROPERTIES
    },
    "WeeklyHospVaccPersonsSexIncomingData": {
        "properties": SWISSDATA_WEEKLY_HOSP_VACC_PERSONS_SEX_INCOMING_DATA_PROPERTIES
    },
    "AdditionalGeoRegionDailyIncomingData": {
        "properties": SWISSDATA_ADDITIONAL_GEO_REGION_DAILY_INCOMING_DATA_PROPERTIES
    },
    "AdditionalGeoRegion14dPeriodIncomingData": {
        "properties": SWISSDATA_ADDITIONAL_GEO_REGION_14D_PERIOD_INCOMING_DATA_PROPERTIES
    },
    "DailyReportIncomingData": {
        "properties": SWISSDATA_DAILY_REPORT_INCOMING_DATA_PROPERTIES
    },
    "ContactTracingIncomingData": {
        "properties": SWISSDATA_CONTACT_TRACING_INCOMING_DATA_PROPERTIES
    },
    "HospCapacityDailyIncomingData": {
        "properties": SWISSDATA_HOSP_CAPACITY_DAILY_INCOMING_DATA_PROPERTIES
    },
    "InternationalQuarantineIncomingData": {
        "properties": SWISSDATA_INTERNATIONAL_QUARANTINE_INCOMING_DATA_PROPERTIES
    },
    "InternationalDailyIncomingData": {
        "properties": SWISSDATA_INTERNATIONAL_DAILY_INCOMING_DATA_PROPERTIES
    },
    "ReDailyIncomingData": {
        "properties": SWISSDATA_REDAILY_INCOMING_DATA_PROPERTIES
    },
    "VaccinationIncomingData": {
        "properties": SWISSDATA_VACCINATION_INCOMING_DATA_PROPERTIES
    },
    "VaccinationDosesReceivedDeliveredVaccineIncomingData": {
        "properties": SWISSDATA_VACCINATION_DOSES_RECEIVED_DELIVERED_VACCINE_INCOMING_DATA_PROPERTIES
    },
    "VaccPersonsIncomingData": {
        "properties": SWISSDATA_VACC_PERSONS_INCOMING_DATA_PROPERTIES
    },
    "VaccPersonsVaccineIncomingData": {
        "properties": SWISSDATA_VACC_PERSONS_VACCINE_INCOMING_DATA_PROPERTIES
    },
    "VaccinationWeeklyIncomingData": {
        "properties": SWISSDATA_VACCINATION_WEEKLY_INCOMING_DATA_PROPERTIES
    },
    "VaccPersonsWeeklyIncomingData": {
        "properties": SWISSDATA_VACC_PERSONS_WEEKLY_INCOMING_DATA_PROPERTIES
    },
    "VaccPersonsWeeklyAgeRangeVaccineIncomingData": {
        "properties": SWISSDATA_VACC_PERSONS_WEEKLY_AGE_RANGE_VACCINE_INCOMING_DATA_PROPERTIES
    },
    "VaccPersonsWeeklyIndicationIncomingData": {
        "properties": SWISSDATA_VACC_PERSONS_WEEKLY_INDICATION_INCOMING_DATA_PROPERTIES
    },
    "VaccinationWeeklyIndicationIncomingData": {
        "properties": SWISSDATA_VACCINATION_WEEKLY_INDICATION_INCOMING_DATA_PROPERTIES
    },
    "VaccinationWeeklyLocationIncomingData": {
        "properties": SWISSDATA_VACCINATION_WEEKLY_LOCATION_INCOMING_DATA_PROPERTIES
    },
    "VaccinationSymptomsIncomingData": {
        "properties": SWISSDATA_VACCINATION_SYMPTOMS_INCOMING_DATA_PROPERTIES
    },
    "VaccinationContingentIncomingData": {
        "properties": SWISSDATA_VACCINATION_CONTINGENT_INCOMING_DATA_PROPERTIES
    },
    "CovidCertificatesDailyIncomingData": {
        "properties": SWISSDATA_COVID_CERTIFICATE_DAILY_INCOMING_DATA_PROPERTIES

    }
}

# endregion DATA
