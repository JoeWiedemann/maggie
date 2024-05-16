# Author: Joe Wiedemann

# This function will demonstrate the basic capacity to read temperatures from the Lakeshore 224 Temperature Monitor
# and write them to the influxDB database. This data will then be pulled onto the Grafana display at http://localhost:3000/

# This updated version queries for the voltage instead of temperature

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

channels = ["CHA","CHB","CHC1", "CHC2", "CHC3", "CHC4"]

loc = "Cooldown1 HK"
def writedata():
	for p in range(0,50):  
		# Measure temps and voltages
		temps = [my_instrument.get_kelvin_reading(chan[2:]) for chan in channels]
		volts = [my_instrument.get_sensor_reading(chan[2:]) for chan in channels]
		
		points_temp = [influxdb_client.Point(loc).tag("source", chan).field("Kelvin", temp) for chan,temp in zip(channels,temps)]
		points_volt = [influxdb_client.Point(loc).tag("source", chan).field("Voltage", volt) for chan,volt in zip(channels,volts)]

		for p in points_temp:
			write_api.write(bucket=bucket, org=org, record= p)
		for p in points_volt:
			write_api.write(bucket=bucket, org=org, record= p)
		

while(1):
	writedata()
	#time.sleep(30)