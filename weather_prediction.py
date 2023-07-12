from datetime import datetime, timedelta
from meteostat import Point, Daily
import numpy as np
from sklearn.linear_model import LinearRegression

# Set time period
start = datetime(2018, 1, 1)
end = datetime.today()

# Create Point for Waterloo, ON
location = Point(43.4643, -80.5204, 329)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()


# # Plot line chart including average, minimum and maximum temperature
# data.plot(y=['tavg', 'tmin', 'tmax'])
# plt.show()

#  Import data into numpy
train_data = np.array(data[['tavg', 'tmin', 'tmax']].values)

# Define sequence length in days
n = 14
train_data_x = []
train_data_y = []

for i in range(len(train_data)-n+1):
    train_data_x.append(train_data[i:i+n-1].flatten())
    train_data_y.append(train_data[i+n-1])

train_data_x = np.array(train_data_x)
train_data_y = np.array(train_data_y)

reg = LinearRegression().fit(train_data_x, train_data_y)

pred = reg.predict(train_data[-n+1:].flatten()[np.newaxis, :])[0]

print(f'{end.date()+timedelta(days=1)} Avg:{round(pred[0], 1)}, Min:{round(pred[1], 1)}, Max:{round(pred[2], 1)}')

