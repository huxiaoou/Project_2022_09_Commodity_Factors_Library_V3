from custom.XClasses import os, pd, dt, List, Dict
from custom.XClasses import CManagerLibWriterByDate, CLib1Tab1


def factors_algorithm_VOL(
        vol_window: int,
        concerned_instruments_universe: List[str],
        database_structure: Dict[str, CLib1Tab1],
        factors_exposure_dir: str,
        md_bgn_date: str,
        md_stp_date: str,
        major_return_dir: str,
        price_type: str = "close",
        MONEY_SCALE: int = 1E8,
):
    factor_lbl = "VOL{:03d}".format(vol_window)

    # --- calculate factors by instrument
    all_factor_data = {}
    for instrument in concerned_instruments_universe:
        major_return_file = "major_return.{}.{}.csv.gz".format(instrument, price_type)
        major_return_path = os.path.join(major_return_dir, major_return_file)
        major_return_df = pd.read_csv(major_return_path, dtype={"trade_date": str}).set_index("trade_date")
        major_return_df[factor_lbl] = major_return_df["amt"] / MONEY_SCALE
        major_return_df[factor_lbl] = major_return_df[factor_lbl].rolling(window=vol_window).mean()
        all_factor_data[instrument] = major_return_df[factor_lbl]

    # --- reorganize
    all_factor_df = pd.DataFrame(all_factor_data)

    # --- save
    factor_lib_structure = database_structure[factor_lbl]
    factor_lib = CManagerLibWriterByDate(
        t_db_name=factor_lib_structure.m_lib_name,
        t_db_save_dir=factors_exposure_dir
    )
    factor_lib.add_table(t_table=factor_lib_structure.m_tab)
    factor_lib.save_factor_by_date(
        t_table_name=factor_lib_structure.m_tab.m_table_name,
        t_all_factor_df=all_factor_df,
        t_bgn_date=md_bgn_date, t_stp_date=md_stp_date,
    )
    factor_lib.close()

    print("... @ {} factor = {:>12s} calculated".format(dt.datetime.now(), factor_lbl))
    return 0
