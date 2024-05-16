import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np

bucket="L224"
token = "RYKrniSyLGNxGSQA7TLnZSq6xydfANl8EnbgHzVLhLnpc5uD9zz82NZ7R_bEZYgeo0kq2C8aoWTOKU-hkM6B7w=="
org = "PXS-Maggie"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Query script
query_api = client.query_api()
query = 'from(bucket:"L224")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "Cooldown1 HK")\
|> filter(fn:(r) => r.source == "CHA")'#\
#|> filter(fn:(r) => r.field == "Kelvin")'    -- standing hypothesis is this is only required with multiple field, e.g. we include voltages

result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        #results.append((record.get_field(), record.get_value()))
        results.append(record.get_value()) # record.get_time() will give you the time for each data point which could be a useful vector

print(results)
print(np.size(results))
#[("Kelvin", 25.3)]
