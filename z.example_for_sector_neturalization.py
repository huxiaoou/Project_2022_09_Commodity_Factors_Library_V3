import pandas as pd
import itertools as ittl

df = pd.DataFrame({
    "行业分类": ["I1", "I1", "I2", "I2"],
    "原始因子": [100, 80, 32, 8],
    "原始收益": [25, 5, 45, 15],
    "中性因子": [10, -10, 12, -12],
    "中性收益": [10, -10, 15, -15],
}, index=["S1", "S2", "S3", "S4"])

print(df)

for x, y in ittl.product(["原始因子", "中性因子"], ["原始收益", "中性收益"]):
    r = df[[x, y]].corr().loc[x, y]
    print("Corr({:4s},{:4s}) = {:>9.4f}".format(x, y, r))
