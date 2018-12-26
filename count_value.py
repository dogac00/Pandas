import pandas as pd

df = pd.DataFrame({"A": [1,2,3,5,6,7,7,8],
                   "B": [2,4,8,8,8,9,9,9]})

def count_value(df, col, val):
    return df[col].value_counts()[val]    # a function which returns how many times a values is seen in a given column
