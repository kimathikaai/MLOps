from datetime import datetime
from meteostat import Point, Daily
import numpy as np

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
train_data_seq = []
for i in range(len(train_data)-n+1):
    train_data_seq.append(train_data[i:i+n])

train_data_seq = np.array(train_data_seq)
print(train_data_seq.shape)
