# Data Structure

## Instrument Return

## Instrument Corr

## Available Universe

file_name = table_name = "available_universe"

primary key = (trade_date, instrument)

value columns = ("return", "amt", "WGT03", "WGT5")

| trade_date | instrument | return | amt | WGT03 | WGT05 |
|:-----------|:-----------|:-------|:----|:------|:------|
| 20220909   | CU.SHF     | 0.05   | 100 | 98    | 96    |

## Test Return

by (test_window,)

file_name = table_name = "TW003"

primary key = (trade_date, instrument)

value columns = ("value",)

| trade_date | instrument | value |
|:-----------|:-----------|:------|
| 20220909   | CU.SHF     | 0.05  |

## Test Return Neutral

by (test_window, uid) with available universe

file_name = table_name = "TW003.U46"

primary key = (trade_date, instrument)

value columns = ("value",)

| trade_date | instrument | value |
|:-----------|:-----------|:------|
| 20220909   | CU.SHF     | 0.05  |

## Factors Exposure

by (factors,)

file_name = table_name = "RSW252HL063"

primary key = (trade_date, instrument)

value columns = ("value",)

| trade_date | instrument | value |
|:-----------|:-----------|:------|
| 20220909   | CU.SHF     | 0.05  |

## Factors Exposure Neutral

by (factors, uid) with available universe

file_name = table_name = "RSW252HL063.U46"

primary key = (trade_date, instrument)

value columns = ("value",)

| trade_date | instrument | value |
|:-----------|:-----------|:------|
| 20220909   | CU.SHF     | 0.05  |

## Factors Exposure Norm and Delinear

by (uid, pid) from Factors Neutral

### Norm

file_name = table_name = "U46.P3.NORM"

primary key = (trade_date, instrument)

value columns = from PID

| trade_date | instrument | RSW252HL063 | BASIS |
|:-----------|:-----------|:------------|:------|
| 20220909   | CU.SHF     | 0.05        | -0.02 |

### Delinear

file_name = table_name = "U46.P3.DELINEAR"

primary key = (trade_date, instrument)

value columns = from PID

| trade_date | instrument | RSW252HL063 | BASIS  |
|:-----------|:-----------|:------------|:-------|
| 20220909   | CU.SHF     | 0.035       | -0.035 |

## Factors Return

by (uid, pid, test_window) from Factors Delinear

file_name = table_name = "U46.P3.TW005"

### factor return

primary key = (trade_date, factor)

value columns = ("return", )

| trade_date | factor      | return |
|:-----------|:------------|:-------|
| 20220909   | RSW252HL063 | 3.14   |

### instrument residual

primary key = (trade_date, instrument)

value columns = ("residual", )

| trade_date | instrument | residual |
|:-----------|:-----------|:---------|
| 20220909   | CU.SHF     | 0.005    |

### pure factor portfolio weight

primary key = (trade_date, instrument)

value columns = from PID

| trade_date | instrument | RSW252HL063 | BASIS |
|:-----------|:-----------|:------------|:------|
| 20220909   | CU.SHF     | 0.08        | 0.92  |
