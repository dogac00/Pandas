import pandas as pd

# import the libray

d = {'foo': [100,101,102], '^bar': [200,201,202]}

# create the dictionary

df = pd.DataFrame(d)

# pass the dictionary to the pandas dataframe

df.loc[df.foo == 101]

# the the row where foo is equal to 101
