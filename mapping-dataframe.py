import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')

train['Sex_Male'] = train.Sex.map('female': 0, 'male': 1)

# We create a new column in the dataframe to show whether the passanger is male or female
# and we did this by mapping the dataframe column

train.head()

# You can see the head of the dataframe, and see the new Sex_Male column at the right

# In another way, you can do this by get_dummies method below

pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:]

# It seems like more work, but it is more flexible than mapping

# iloc is used to select all rows and second column
# train.Sex is a Series, prefix is a name before the sex eg. Sex_male
