import os
import sys
import datetime as dt
import numpy as np
import pandas as pd
import itertools as ittl
from skyrim.winterhold import check_and_mkdir, plot_corr, plot_lines
from skyrim.whiterun import CCalendar, CInstrumentInfoTable
from skyrim.configurationOffice import SKYRIM_CONST_CALENDAR_PATH, SKYRIM_CONST_INSTRUMENT_INFO_PATH

"""
Project: Project_2022_09_Commodity_Factors_Library_V3
Author : HUXO
Created: 10:32, 周三, 2022/9/14
"""

pd.set_option("display.width", 0)
pd.set_option("display.float_format", "{:.2f}".format)

# --- project data settings
data_root_dir = os.path.join("/Data")
project_name = os.getcwd().split("\\")[-1]
project_data_dir = os.path.join(data_root_dir, project_name)
if not os.path.exists(project_data_dir):
    os.mkdir(project_data_dir)
instruments_return_dir = os.path.join(project_data_dir, "instruments_return")
instruments_corr_dir = os.path.join(project_data_dir, "instruments_corr")
available_universe_dir = os.path.join(project_data_dir, "available_universe")
test_return_dir = os.path.join(project_data_dir, "test_return")
test_return_neutral_dir = os.path.join(project_data_dir, "test_return_neutral")
factors_exposure_dir = os.path.join(project_data_dir, "factors_exposure")
factors_exposure_neutral_dir = os.path.join(project_data_dir, "factors_exposure_neutral")
factors_exposure_corr_dir = os.path.join(project_data_dir, "factors_exposure_corr")
test_ic_dir = os.path.join(project_data_dir, "test_ic")

# --- database settings
DATABASE = os.path.join("/Database")
futures_dir = os.path.join(DATABASE, "Futures")
futures_instrument_mkt_data_dir = os.path.join(futures_dir, "instrument_mkt_data")
major_minor_dir = os.path.join(futures_dir, "by_instrument", "major_minor")
major_return_dir = os.path.join(futures_dir, "by_instrument", "major_return")
md_dir = os.path.join(futures_dir, "by_instrument", "md")
index_dir = os.path.join(futures_dir, "by_instrument", "index", "CUSTOM")
extra_data_dir = os.path.join(futures_dir, "by_instrument", "extra_data")
