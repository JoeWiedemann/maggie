import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

bucket="test"
token = "RYKrniSyLGNxGSQA7TLnZSq6xydfANl8EnbgHzVLhLnpc5uD9zz82NZ7R_bEZYgeo0kq2C8aoWTOKU-hkM6B7w=="
org = "PXS-Maggie"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)
   
def writedata(start_val):
	for p in range(0,50):
		float(start_val)
		p = influxdb_client.Point("test_measurement").tag("temperatures", "50K diode").field("degree Kelvin", start_val)
		start_val+= 1
		write_api.write(bucket=bucket, org=org, record=p)
		print(p)
		time.sleep(5) # separate points by 5 seconds

while(1):
	writedata(0.1)
	time.sleep(30)

#p = influxdb_client.Point("test_measurement").tag("temperatures", "40K diode").field("degree Kelvin", pp)
#write_api.write(bucket=bucket, org=org, record=p)

