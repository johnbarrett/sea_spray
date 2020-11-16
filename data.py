import pandas as pd

# load & read csv file
content = pd.read_csv('data/ssaSlice.csv', header=0)

# converting the old date format from the kite to datetime format
content['date'] = pd.to_datetime(content['date'])
content['timedate'] = pd.to_datetime(content['timedate'])
content['end_time'] = pd.to_datetime(content['end_time'])

# skip the header
# next(df)
# print the csv to the terminal
# print(content.columns)

single_column = content["date"]
print(content.loc[2:7, :])

# print(single_column)
# print(content)
