# load the necessary libraries
import pandas as pd

# load & read csv file
content = pd.read_csv('data/ssaSlice.csv', header=0)

# converting the old date format from the kite to datetime format
content['date'] = pd.to_datetime(content['date'])
content['timedate'] = pd.to_datetime(content['timedate'])
content['end_time'] = pd.to_datetime(content['end_time'])

# print information about the columns
print(content.info())
print(content)


print(content.columns)

subset = content.loc[:, ["lat", "lon"]]
print(subset)
