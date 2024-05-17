import maggie_functions as mf

# Import indluxDB functions
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Define where to write the data - must have set up DBRP for bucket
bucket="L224"
token = "RYKrniSyLGNxGSQA7TLnZSq6xydfANl8EnbgHzVLhLnpc5uD9zz82NZ7R_bEZYgeo0kq2C8aoWTOKU-hkM6B7w=="
org = "PXS-Maggie"
url = "http://localhost:8086"
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)


KY_channels = ["CH1","CH2","CH3"]

loc = "Cooldown2 HK"
def getdata():	
    for ky_chan in KY_channels:
        pc_temp = mf.ky("current", ky_chan)
        pc = influxdb_client.Point(loc).tag("source", ky_chan).field("current", pc_temp)
        write_api.write(bucket=bucket, org=org, record= pc)
        
        pv_temp = mf.ky("voltage", ky_chan)
        pv = influxdb_client.Point(loc).tag("source", ky_chan).field("volterinos", pc_temp)
        write_api.write(bucket=bucket, org=org, record= pv)

while(1):
	getdata()