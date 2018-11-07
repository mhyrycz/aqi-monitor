import miio
import time
import logging
from influxdb import InfluxDBClient

def write_data(ip, token, series):
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    device = miio.airqualitymonitor.AirQualityMonitor(ip=f'{ip}',
                                                      token=f'{token}',
                                                      start_id=0,
                                                      debug=0,
                                                      lazy_discover=True)

    device.on()
    logging.info('Turned on')
    time.sleep(20)
    air_status = device.status().aqi
    timestamp = [
        {
            "measurement": f"{series}",
            "fields": {
                "aqi": air_status
            }
        }
    ]
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'xiaomi')
    written_data = client.write_points(timestamp)
    logging.info(f'{written_data}')
    device.off()

write_data('192.168.0.101', 'e1ad2a2d4343fedd0c558ff49d261510', 'pm25')
write_data('192.168.0.206', '7aaf72414d8606bff08feeb655afe0fb', 'purifier')
