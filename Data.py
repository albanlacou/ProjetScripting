import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import CPU.psutilCPU as CPU

token = os.environ.get("INFLUXDB_TOKEN")
org = "loic.gouriou@edu.itescia.fr"
url = "http://192.168.1.40:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


write_api = client.write_api(write_options=SYNCHRONOUS)
"""
return rien 
ajoute les valeurs a notre measurement
"""
def write_db(donne):
        point = (
            Point("composant")
            .tag("type", "value")
            .field(donne[0], donne[1])
        )
        write_api.write(bucket=bucket, url='http://192.168.1.40:8086', record=point)
        time.sleep(1)  # separate points by 1 second