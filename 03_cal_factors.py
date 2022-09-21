from setup import *
from custom.factors_algorithm_BASIS import factors_algorithm_BASIS
from custom.factors_algorithm_BETA import factors_algorithm_BETA
from custom.factors_algorithm_CTP import factors_algorithm_CTP
from custom.factors_algorithm_CV import factors_algorithm_CV
from custom.factors_algorithm_HP import factors_algorithm_HP
from custom.factors_algorithm_MTM import factors_algorithm_MTM
from custom.factors_algorithm_RSW import factors_algorithm_RSW
from custom.factors_algorithm_SIZE import factors_algorithm_SIZE
from custom.factors_algorithm_TS import factors_algorithm_TS
from configure import concerned_instruments_universe, database_structure, md_bgn_date, md_stp_date

instrument_info_table = CInstrumentInfoTable(t_path=SKYRIM_CONST_INSTRUMENT_INFO_PATH, t_index_label="windCode")

# factors_algorithm_BASIS(
#     basis_window=147,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     extra_data_dir=extra_data_dir,
#     major_minor_dir=major_minor_dir
# )

# factors_algorithm_BETA(
#     beta_window=252,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     instruments_return_dir=instruments_return_dir,
#     major_return_dir=major_return_dir,
# )
#
# factors_algorithm_CV(
#     cv_window=252,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     major_return_dir=major_return_dir
# )

# factors_algorithm_CTP(
#     ctp_window=63,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     major_return_dir=major_return_dir,
# )

# factors_algorithm_HP(
#     hp_window=189,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     major_return_dir=major_return_dir
# )


# factors_algorithm_MTM(
#     mtm_window=252,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     index_dir=index_dir,
# )
#
# factors_algorithm_RSW(
#     rs_window=252, half_life=63,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     extra_data_dir=extra_data_dir,
#     major_minor_dir=major_minor_dir,
# )

# factors_algorithm_SIZE(
#     size_window=252,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     major_return_dir=major_return_dir,
#     instrument_info_table=instrument_info_table
# )

# factors_algorithm_TS(
#     ts_window=126,
#     concerned_instruments_universe=concerned_instruments_universe,
#     database_structure=database_structure,
#     factors_exposure_dir=factors_exposure_dir,
#     md_bgn_date=md_bgn_date,
#     md_stp_date=md_stp_date,
#     major_minor_dir=major_minor_dir,
#     md_dir=md_dir,
# )
