import pandas as pd

df = pd.DataFrame({"A": [1,2,3,5,6,7,7,8],
                   "B": [2,4,8,8,8,9,9,9]})

def add_square(df, col):
    df = df.assign(C = df[col]**2)    # a function that adds a squared version of a specific column to a dataframe
    return df
