from setup import *
from custom.factors_algorithm_BASIS import factors_algorithm_BASIS
from configure import concerned_instruments_universe, database_structure, md_bgn_date, md_stp_date

factors_algorithm_BASIS(
    basis_window=147,
    concerned_instruments_universe=concerned_instruments_universe,
    database_structure=database_structure,
    factors_exposure_dir=factors_exposure_dir,
    md_bgn_date=md_bgn_date,
    md_stp_date=md_stp_date,
    extra_data_dir=extra_data_dir,
    major_minor_dir=major_minor_dir
)
