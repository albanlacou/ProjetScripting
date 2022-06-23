import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import CPU.psutilCPU as CPU

token = "4FDnyvzUa78E_E6kDaluT5wkwf5ijaiWgs1nrxjvbva8tuN1oeAaYVUImYeoXRRsjUBCZNOqS4PqND15pp73NQ=="

org = "belli.kieran@gmail.com"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"

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
        write_api.write(bucket="Logs", org="belli.kieran@gmail.com", record=point)
        time.sleep(1)  # separate points by 1 second