import datetime as dt
from custom.XClasses import CLib1Tab1, CTable, Dict

"""
created @ 2022-05-23
0.  derived from E:\\Works\\2022\\Project_2022_03_Commodity_Factors_Library_V1
1.  remove
        md_stp_date
        factors_stp_date
    these two parameters should be input as script arguments
"""

md_bgn_date, md_stp_date = "20140101", (dt.datetime.now() + dt.timedelta(days=1)).strftime("%Y%m%d")
factors_bgn_date = "20150401"

# universe
concerned_instruments_universe = [
    "AU.SHF",  # "20080109"
    "AG.SHF",  # "20120510"
    "CU.SHF",  # "19950417"
    "AL.SHF",  # "19950417"
    "PB.SHF",  # "20140801"
    "ZN.SHF",  # "20070326"
    "SN.SHF",  # "20151102"
    "NI.SHF",  # "20150327"
    "SS.SHF",  # "20190925"
    "RB.SHF",  # "20090327"
    "HC.SHF",  # "20140321"
    "J.DCE",  # "20110415"
    "JM.DCE",  # "20130322"
    "I.DCE",  # "20131018"
    "FG.CZC",  # "20121203"
    "SA.CZC",  # "20191206"
    "UR.CZC",  # "20190809"
    "ZC.CZC",  # "20151201"
    "SF.CZC",  # "20140808"
    "SM.CZC",  # "20140808"
    "Y.DCE",  # "20060109"
    "P.DCE",  # "20071029"
    "OI.CZC",  # "20130423"
    "M.DCE",  # "20000717"
    "RM.CZC",  # "20121228"
    "A.DCE",  # "19990104"
    "RU.SHF",  # "19950516"
    "BU.SHF",  # "20131009"
    "FU.SHF",  # "20040825"  # re-active since 20180801
    "L.DCE",  # "20070731"
    "V.DCE",  # "20090525"
    "PP.DCE",  # "20140228"
    "EG.DCE",  # "20181210"
    "EB.DCE",  # "20191206"
    "PG.DCE",  # "20200330"
    "TA.CZC",  # "20061218"
    "MA.CZC",  # "20141224"
    "CF.CZC",  # "20040601"
    "CY.CZC",  # "20170808"
    "SR.CZC",  # "20060106"
    "C.DCE",  # "20040922"
    "CS.DCE",  # "20141219"
    "SP.SHF",  # "20181127"
    "JD.DCE",  # "20131108"
    "AP.CZC",  # "20171222"
    "CJ.CZC",  # "20190430"
]
ciu_size = len(concerned_instruments_universe)  # should be 46

# available universe
available_universe_rolling_window = 20
available_universe_amt_threshold = 5

# sector
sector_list = ["AUAG", "METAL", "BLACK", "OIL", "CHEM", "MISC"]  # 6
sector_classification = {
    "AU.SHF": "AUAG",
    "AG.SHF": "AUAG",
    "CU.SHF": "METAL",
    "AL.SHF": "METAL",
    "PB.SHF": "METAL",
    "ZN.SHF": "METAL",
    "SN.SHF": "METAL",
    "NI.SHF": "METAL",
    "SS.SHF": "METAL",
    "RB.SHF": "BLACK",
    "HC.SHF": "BLACK",
    "J.DCE": "BLACK",
    "JM.DCE": "BLACK",
    "I.DCE": "BLACK",
    "FG.CZC": "BLACK",
    "SA.CZC": "BLACK",
    "UR.CZC": "BLACK",
    "ZC.CZC": "BLACK",
    "SF.CZC": "BLACK",
    "SM.CZC": "BLACK",
    "Y.DCE": "OIL",
    "P.DCE": "OIL",
    "OI.CZC": "OIL",
    "M.DCE": "OIL",
    "RM.CZC": "OIL",
    "A.DCE": "OIL",
    "RU.SHF": "CHEM",
    "BU.SHF": "CHEM",
    "FU.SHF": "CHEM",
    "L.DCE": "CHEM",
    "V.DCE": "CHEM",
    "PP.DCE": "CHEM",
    "EG.DCE": "CHEM",
    "EB.DCE": "CHEM",
    "PG.DCE": "CHEM",
    "TA.CZC": "CHEM",
    "MA.CZC": "CHEM",
    "CF.CZC": "MISC",
    "CY.CZC": "MISC",
    "SR.CZC": "MISC",
    "C.DCE": "MISC",
    "CS.DCE": "MISC",
    "SP.SHF": "MISC",
    "JD.DCE": "MISC",
    "AP.CZC": "MISC",
    "CJ.CZC": "MISC",
}

# --- factor settings ---
# total number of factors =
basis_window_list = [105, 126, 147]  # 3
beta_window_list = [10, 21, 63, 126, 189, 252]  # 6
cv_window_list = [10, 21, 63, 126, 189, 252]  # 6
csp_window_list = [10, 21, 63, 126, 189, 252]  # 6
csr_window_list = [10, 21, 63, 126, 189, 252]  # 6
ctp_window_list = [10, 21, 63, 126, 189, 252]  # 6
ctr_window_list = [10, 21, 63, 126, 189, 252]  # 6
cvp_window_list = [10, 21, 63, 126, 189, 252]  # 6
cvr_window_list = [10, 21, 63, 126, 189, 252]  # 6
hp_window_list = [10, 21, 63, 126, 189, 252]  # 6
mtm_window_list = [10, 21, 63, 126, 189, 231, 252]  # 7
rsw_half_life_window_list = [21, 63, 126]  # 3
sgm_window_list = [10, 21, 63, 126, 189, 252]  # 6
size_window_list = [10, 21, 63, 126, 189, 252]  # 6
skew_window_list = [10, 21, 63, 126, 189, 252]  # 6
to_window_list = [10, 21, 63, 126, 189, 252]  # 6
ts_window_list = [10, 21, 63, 126, 189, 252]  # 6
vol_window_list = [10, 21, 63, 126, 189, 252]  # 6

factor_list = ["BASIS{:03d}".format(z) for z in basis_window_list] \
              + ["BETA{:03d}".format(z) for z in beta_window_list] \
              + ["CV{:03d}".format(z) for z in cv_window_list] \
              + ["CSP{:03d}".format(z) for z in csp_window_list] \
              + ["CSR{:03d}".format(z) for z in csr_window_list] \
              + ["CTP{:03d}".format(z) for z in ctp_window_list] \
              + ["CTR{:03d}".format(z) for z in ctr_window_list] \
              + ["CVP{:03d}".format(z) for z in cvp_window_list] \
              + ["CVR{:03d}".format(z) for z in cvr_window_list] \
              + ["HP{:03d}".format(z) for z in hp_window_list] \
              + ["MTM{:03d}".format(z) for z in mtm_window_list] \
              + ["RSW{:03d}HL{:03d}".format(252, z) for z in rsw_half_life_window_list] \
              + ["SGM{:03d}".format(z) for z in sgm_window_list] \
              + ["SIZE{:03d}".format(z) for z in size_window_list] \
              + ["SKEW{:03d}".format(z) for z in skew_window_list] \
              + ["TO{:03d}".format(z) for z in to_window_list] \
              + ["TS{:03d}".format(z) for z in to_window_list] \
              + ["VOL{:03d}".format(z) for z in vol_window_list]

# --- test return ---
test_window_list = [3, 5, 10, 15, 20]  # 5
test_lag = 1

# --- instrument universe ---
instruments_universe_options = {
    "U46": concerned_instruments_universe,  # size = 46
    "U29": [
        "CU.SHF",  # "19950417"
        "AL.SHF",  # "19950417"
        "PB.SHF",  # "20140801"
        "ZN.SHF",  # "20070326"
        "SN.SHF",  # "20151102"
        "NI.SHF",  # "20150327"
        "RB.SHF",  # "20090327"
        "HC.SHF",  # "20140321"
        "J.DCE",  # "20110415"
        "JM.DCE",  # "20130322"
        "I.DCE",  # "20131018"
        "FG.CZC",  # "20121203"
        "Y.DCE",  # "20060109"
        "P.DCE",  # "20071029"
        "OI.CZC",  # "20130423"
        "M.DCE",  # "20000717"
        "RM.CZC",  # "20121228"
        "A.DCE",  # "19990104"
        "RU.SHF",  # "19950516"
        "BU.SHF",  # "20131009"
        "L.DCE",  # "20070731"
        "V.DCE",  # "20090525"
        "PP.DCE",  # "20140228"
        "TA.CZC",  # "20061218"
        "MA.CZC",  # "20141224"
        "CF.CZC",  # "20040601"
        "SR.CZC",  # "20060106"
        "C.DCE",  # "20040922"
        "CS.DCE",  # "20141219"
    ],  # size = 29
    "U23": [
        "RB.SHF",  # "20090327"
        "HC.SHF",  # "20140321"
        "J.DCE",  # "20110415"
        "JM.DCE",  # "20130322"
        "I.DCE",  # "20131018"
        "FG.CZC",  # "20121203"
        "Y.DCE",  # "20060109"
        "P.DCE",  # "20071029"
        "OI.CZC",  # "20130423"
        "M.DCE",  # "20000717"
        "RM.CZC",  # "20121228"
        "A.DCE",  # "19990104"
        "RU.SHF",  # "19950516"
        "BU.SHF",  # "20131009"
        "L.DCE",  # "20070731"
        "V.DCE",  # "20090525"
        "PP.DCE",  # "20140228"
        "TA.CZC",  # "20061218"
        "MA.CZC",  # "20141224"
        "CF.CZC",  # "20040601"
        "SR.CZC",  # "20060106"
        "C.DCE",  # "20040922"
        "CS.DCE",  # "20141219"
    ],  # size = 23
}

# --- factors pool ---
factors_pool_options = {
    "P3": ["BETA252", "SIZE252", "CV252", "SKEW126", "MTM231", "RSW252HL063", "BASIS147", "CTP063"],
}

# risk_factors_pool_options = {
#     "P0": ["BETA252", "SIZE252", "CV252", "SKEW126"],
#     "P1": ["SIZE252", "CV252", "SKEW126"],
#     "P2": ["BETA252", "SIZE252", "CV252", "SKEW126"],
# }

# secondary parameters
RETURN_SCALE = 100
YIYUAN = 1e8
days_per_year = 252
price_type = "close"

# aux
default_start_date = "20120101"
start_date_settings = {
    "BU.SHF": "20150401",
    "ZC.CZC": "20151201",
}

# database
database_structure: Dict[str, CLib1Tab1] = {
    "available_universe": CLib1Tab1(
        t_lib_name="available_universe.db",
        t_tab=CTable(
            t_table_name="available_universe",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={**{"return": "REAL", "amt": "REAL"}, **{"WGT{:02d}".format(z): "REAL" for z in test_window_list}}
        )),

    "test_return_003": CLib1Tab1(
        t_lib_name="test_return_003.db",
        t_tab=CTable(
            t_table_name="test_return_003",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        )),

    "test_return_005": CLib1Tab1(
        t_lib_name="test_return_005.db",
        t_tab=CTable(
            t_table_name="test_return_005",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        )),

    "test_return_010": CLib1Tab1(
        t_lib_name="test_return_010.db",
        t_tab=CTable(
            t_table_name="test_return_010",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        )),

    "test_return_015": CLib1Tab1(
        t_lib_name="test_return_015.db",
        t_tab=CTable(
            t_table_name="test_return_015",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        )),

    "test_return_020": CLib1Tab1(
        t_lib_name="test_return_020.db",
        t_tab=CTable(
            t_table_name="test_return_020",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        )
    ),

    "BASIS147": CLib1Tab1(
        t_lib_name="BASIS147.db",
        t_tab=CTable(
            t_table_name="BASIS147",
            t_primary_keys={"trade_date": "TEXT", "instrument": "TEXT"},
            t_value_columns={"value": "REAL"},
        ))
}
