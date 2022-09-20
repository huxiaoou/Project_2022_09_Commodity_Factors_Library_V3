from setup import *
from configure import test_window_list, instruments_universe_options
from configure import database_structure, md_bgn_date, md_stp_date
from configure import sector_classification
from custom.XClasses import CManagerLibReader, CManagerLibWriterByDate
from custom.XFuns import neutralize_by_sector

cne_calendar = CCalendar(t_path=SKYRIM_CONST_CALENDAR_PATH)

available_universe_lib_structure = database_structure["available_universe"]
available_universe_lib = CManagerLibReader(t_db_name=available_universe_lib_structure.m_lib_name, t_db_save_dir=available_universe_dir)

for test_window, uid in ittl.product(test_window_list, instruments_universe_options.keys()):
    weight_id = "WGT{:02d}".format(test_window)

    # mother universe
    mother_universe = instruments_universe_options[uid]
    mother_universe_df = pd.DataFrame({"instrument": mother_universe})

    # sector df
    sector_df = pd.DataFrame.from_dict({z: {sector_classification[z]: 1} for z in mother_universe}, orient="index").fillna(0)

    # test return library
    test_return_lib_id = "test_return_{:03d}".format(test_window)
    test_return_lib_structure = database_structure[test_return_lib_id]
    test_return_lib = CManagerLibReader(t_db_name=test_return_lib_structure.m_lib_name, t_db_save_dir=test_return_dir)

    # test return neutral library
    test_return_neutral_lib_id = "test_return_neutral_{:03d}.{}".format(test_window, uid)
    test_return_neutral_lib_structure = database_structure[test_return_neutral_lib_id]
    test_return_neutral_lib = CManagerLibWriterByDate(t_db_name=test_return_neutral_lib_structure.m_lib_name, t_db_save_dir=test_return_dir)
    test_return_neutral_lib.add_table(t_table=test_return_neutral_lib_structure.m_tab)

    # update by date
    for trade_date in cne_calendar.get_iter_list(t_bgn_date=md_bgn_date, t_stp_date=md_stp_date, t_ascending=True):
        test_return_df = test_return_lib.read_by_date(
            t_table_name=test_return_lib_structure.m_tab.m_table_name,
            t_trade_date=trade_date,
            t_value_columns=["instrument", "value"]
        )

        if len(test_return_df) > 0:
            weight_df = available_universe_lib.read_by_date(
                t_table_name=available_universe_lib_structure.m_tab.m_table_name,
                t_trade_date=trade_date,
                t_value_columns=["instrument", weight_id]
            )

            input_df = pd.merge(
                left=mother_universe_df, right=weight_df,
                on=["instrument"], how="inner"
            ).merge(right=test_return_df, how="left", on=["instrument"]).set_index("instrument")

            test_return_neutral_srs = neutralize_by_sector(
                t_raw_data=input_df["value"],
                t_sector_df=sector_df,
                t_weight=input_df[weight_id]
            )

            test_return_neutral_lib.update_by_date(
                t_table_name=test_return_neutral_lib_structure.m_tab.m_table_name,
                t_date=trade_date,
                t_update_df=pd.DataFrame({"value": test_return_neutral_srs}),
                t_using_index=True
            )

    test_return_lib.close()
    test_return_neutral_lib.close()

    print("... @ {} Neutralization for test return {:03d} of {} calculated.".format(
        dt.datetime.now(), test_window, uid
    ))
