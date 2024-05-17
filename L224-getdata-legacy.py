# Author: Joe Wiedemann

# This function will demonstrate the basic capacity to read temperatures from the Lakeshore 224 Temperature Monitor
# and write them to the influxDB database. This data will then be pulled onto the Grafana display at http://localhost:3000/

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
   
# Lakeshore package directly supports model 224
from lakeshore import Model224

my_instrument = Model224()

def writedata(start_val):
	for p in range(0,50):
		float(start_val)
		tempA = my_instrument.get_kelvin_reading('A')
		tempB = my_instrument.get_kelvin_reading('B')
		PA = influxdb_client.Point("temperature measurement").tag("source", "CHA").field("degree Kelvin", tempA)
		PB = influxdb_client.Point("temperature measurement").tag("source", "CHB").field("degree Kelvin", tempB)
		start_val+= 1
		write_api.write(bucket=bucket, org=org, record=PA)
		write_api.write(bucket=bucket, org=org, record=PB)
		time.sleep(1) # separate points by 5 seconds



while(1):
	writedata(0)
	#time.sleep(30)