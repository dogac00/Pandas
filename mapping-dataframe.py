import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')

train['Sex_Male'] = train.Sex.map('female': 0, 'male': 1)

# We create a new column in the dataframe to show whether the passanger is male or female
# and we did this by mapping the dataframe column

train.head()

# You can see the head of the dataframe, and see the new Sex_Male column at the right
