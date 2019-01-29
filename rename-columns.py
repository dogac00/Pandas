import pandas as pd

df = pd.DataFrame({'$a':[1,2], '$b': [10,20]})

# create the dataframe

df.columns = ['a', 'b']

# assign new columns to the df.columns attribute

df.head()
