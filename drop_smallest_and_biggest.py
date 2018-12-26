import pandas as pd

df = pd.DataFrame({"A": [1,2,3,5,6,7,7,8],
                   "B": [2,4,8,8,8,9,9,9]})

def drop_smallest_and_biggest(df, col):
    df = df.drop(df.idxmax()[col])      # a function which finds smallest and biggest numbers in a column and drops them out
    df = df.drop(df.idxmin()[col])
    return df
