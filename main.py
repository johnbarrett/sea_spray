# load the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load & read csv file
content = pd.read_csv('data/ssaSlice.csv', header=0)

# converting the old date format from the kite to datetime format
content['date'] = pd.to_datetime(content['date'])
content['timedate'] = pd.to_datetime(content['timedate'])
content['end_time'] = pd.to_datetime(content['end_time'])

# print Data Frame
print(content)

# print only 2 columns
subset = content.loc[:, ["lon", "lat"]]
print(subset)

# Make plot of the data
subset.plot(x='lon', y='lat', kind='scatter')
plt.title("Kite's Flight")
plt.ylabel('lat')

plt.show()
