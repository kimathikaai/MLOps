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


def test_NaN():
    assert np.sum(np.isnan(data[['tavg', 'tmin', 'tmax']].values)) == 0

