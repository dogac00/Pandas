import pandas as pd

df = pd.DataFrame({"A": [1,2,3,5,6,7,7,8],
                   "B": [2,4,8,8,8,9,9,9]})

def drop_column(df, col):
    df = df.drop(columns=[col])     # a function which drops a specific column from a dataframe
    return df

