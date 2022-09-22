from configure import factors_list, test_window_list
from configure import instruments_universe_options
from threading import Thread
import subprocess
from custom.XFuns import product, fun_for_test_ic, fun_for_test_neutral_ic

switch = {
    "factor": False,
    "ic_test": True,
    "ic_test_neutral": True,
    "delinear": False,
    "factor_return": False,
}

if switch["factor"]:
    subprocess.run(["python", "03_cal_factors.py"])
    subprocess.run(["python", "03_cal_factors_neutral.py"])

if switch["ic_test"]:
    target_factor_list = factors_list
    gn = 3
    join_list = []
    for group_id in range(gn):
        t = Thread(target=fun_for_test_ic, args=(group_id, gn, target_factor_list, test_window_list))
        t.start()
        join_list.append(t)
    for t in join_list:
        t.join()

    for factor in target_factor_list:
        subprocess.run(["python", "04_B_factor_test_ic_plot.py", factor])

if switch["ic_test_neutral"]:
    target_factor_list = factors_list
    target_uid_list = list(instruments_universe_options.keys())
    gn = 3
    join_list = []
    for group_id in range(gn):
        t = Thread(target=fun_for_test_neutral_ic, args=(group_id, gn, target_factor_list, target_uid_list, test_window_list))
        t.start()
        join_list.append(t)
    for t in join_list:
        t.join()

    for factor, uid in product(target_factor_list, target_uid_list):
        subprocess.run(["python", "04_B_factor_test_neutral_ic_plot.py", factor, uid])

if switch["delinear"]:
    # fun_for_normalize_delinear(
    #     t_uid_list=list(instruments_universe_options.keys()),
    #     t_pid_list=list(factors_pool_options.keys()),
    #     t_factor_stp_date="20220809"
    # )
    pass

if switch["factor_return"]:
    pass
    # fun_for_factor_return(
    #     t_uid_list=list(instruments_universe_options.keys()),
    #     t_pid_list=list(factors_pool_options.keys()),
    #     t_test_window_list=test_window_list,
    #     t_factor_stp_date="20220809",
    # )
    #
    # fun_for_factor_return_agg(
    #     t_uid_list=list(instruments_universe_options.keys()),
    #     t_pid_list=list(factors_pool_options.keys()),
    #     t_test_window_list=test_window_list,
    #     t_factor_stp_date="20220809",
    # )
