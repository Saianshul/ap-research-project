import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3]
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7]
)

df3 = pd.DataFrame(
    {
        "A": ["A9", "A10", "A11", "A12"],
        "B": ["B9", "B10", "B11", "B12"],
        "C": ["C9", "C10", "C11", "C12"],
        "D": ["D9", "D10", "D11", "D12"],
    }
)

df4 = pd.DataFrame(
    {
        "G": ["G0", "G1", "G2", "G3", "G4", "G5"]
    },
    index=["C2", "C3", "C4", "C5", "C6", "C7"]
)

s1 = pd.Series(["E0", "E1", "E2", "E3"], name="E")
s2 = pd.Series(["Z0", "Z1", "Z2", "Z3", "Z4"], index = ["B", "C", "D", "E", "F"])

result1 = pd.concat([df1, df2])
result2 = pd.concat([result1, s1], axis=1)
result3 = pd.concat([result2, s2], ignore_index=True)
# result3 = pd.concat([result2, s2.to_frame().T], ignore_index=True)
result4 = pd.merge(result3, df3, on=["A", "B"], indicator="indicator", suffixes=("_a", "_b"))
# result4 = pd.merge(result3, df3, on=["A", "B"], how="outer", indicator="indicator", suffixes=("_a", "_b"))
final_result = result4.join(df4, on="C_a")

indicies = [
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
]
tuples = list(zip(*indicies))
index = pd.MultiIndex.from_tuples(tuples)
final_result.index = index

# final_result.loc["five", "E"] = "E5"

final_df = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", np.nan, "A9", "A10", "A11", "A12"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "Z0", "B9", "B10", "B11", "B12"],
        "C_a": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "Z1", np.nan, np.nan, np.nan, np.nan],
        "D_a": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "Z2", np.nan, np.nan, np.nan, np.nan],
        "E": ["E0", "E1", "E2", "E3", np.nan, "E5", np.nan, np.nan, "Z3", np.nan, np.nan, np.nan, np.nan],
        "F": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, "Z4", np.nan, np.nan, np.nan, np.nan],
        "C_b": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, "C9", "C10", "C11", "C12"],
        "D_b": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, "D9", "D10", "D11", "D12"],
        "indicator": ["left_only", "left_only", "left_only", "left_only", "left_only", "left_only", "left_only", "left_only", "left_only", "right_only", "right_only", "right_only", "right_only"],
        "G": [np.nan, np.nan, "G0", "G1", "G2", "G3", "G4", "G5", np.nan, np.nan, np.nan, np.nan, np.nan]
    }
)

final_df.index = index

print(final_result.compare(final_df))