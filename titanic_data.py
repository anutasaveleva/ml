import numpy as np
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# Features for plot
features = ['Sex','Age','Survived']
x = data.loc[:,features]

# Drop empty values
x=x.dropna()

# Change sex row in order to save colours for plot
x['Sex']=x['Sex'].map(lambda sex: 'b' if sex == 'male' else 'r')
fig, ax = plt.subplots()
ax.bar(x.index, x['Age'], color=x['Sex'])
ax.set(xlabel='Id', ylabel='Age')
plt.show()

fig = x['Age'].hist()
fig.set(xlabel='Age', ylabel='Count')
plt.show()