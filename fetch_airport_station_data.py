from datetime import datetime
from meteostat import Stations, Hourly

AIRPORT_STATION_ID = 86218

start_date = datetime(2025, 1, 18)
end_date = datetime(2025, 2, 1)

data = Hourly(AIRPORT_STATION_ID, start_date, end_date)
data = data.fetch()
start_date_str = start_date.strftime("%Y_%m_%d")
end_date_str = end_date.strftime("%Y_%m_%d")
data.to_csv(f"./data/airport_station_hourly-{start_date_str}-{end_date_str}.csv")

print(data)
exit()

stations = Stations()
stations = stations.nearby(-25.2416738, -57.5140129)
station = stations.fetch(1)

print(station)