import miio
import time
from influxdb import InfluxDBClient


pm25 = miio.airqualitymonitor.AirQualityMonitor(ip='192.168.0.101',
                                             token='e1ad2a2d4343fedd0c558ff49d261510',
                                             start_id=0,
                                             debug=0,
                                             lazy_discover=True)
pm25.on()
time.sleep(20)
air_status = pm25.status().aqi
timestamp = [
    {
        "measurement": "solarwinds",
        "fields": {
            "aqi": air_status
        }
    }
]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'xiaomi')
client.write_points(timestamp)
pm25.off()
