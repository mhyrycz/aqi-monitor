import miio
from miio.airpurifier import AirPurifier, OperationMode
import time
import logging
from influxdb import InfluxDBClient
#from pudb import set_trace; set_trace()

def establish_connection(xiaomi_type, ip, token):
    device = xiaomi_type(ip=f'{ip}',
                token=f'{token}',
                start_id=0,
                debug=0,
                lazy_discover=True)
    return device


def write_data(device_connected, series):
    if device_connected.status().power == "off":
        device_connected.on()
        time.sleep(20)
        was_turned_on = False
    else:
        was_turned_on = True
    #import pudb; pu.db
    air_status = device_connected.status().aqi
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
    if was_turned_on == False:
        device_connected.off()

write_data(establish_connection(miio.airqualitymonitor.AirQualityMonitor, '192.168.0.101', 'e1ad2a2d4343fedd0c558ff49d261510'),'pm25')
write_data(establish_connection(miio.airpurifier.AirPurifier, '192.168.0.206', '7aaf72414d8606bff08feeb655afe0fb'),'purifier')
