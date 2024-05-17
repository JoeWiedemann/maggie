# Master Fucntions File

# For Power supply, field and chan must be strings 
# field can be current or voltage. chan can be ch1 ch2 ch3
def ky(field,chan):
    import pyvisa
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('USB0::1510::8752::9210309::0::INSTR') # this is serial number specific
    s1 = 'fetch:'
    s2 = '? '
    
    return(float(inst.query(s1+field+s2+chan)))

# For lakeshore 224 diode monitor - returns a float
# field should be kelvin or voltage
# chan can be : CHA, CHB, CHC1-5, CHD1-5
def ls224(field,chan):
    from lakeshore import Model224
    my_instrument = Model224()
    if field == 'kelvin':
        return(float(my_instrument.get_kelvin_reading(chan)))
    else:
        return(float(my_instrument.get_sensor_reading(chan)))


# Preps data point to influxDB
def idb(loc,machine,chan,units,value):
    # Import indluxDB functions
    import influxdb_client, os, time
    from influxdb_client import InfluxDBClient, Point, WritePrecision
    from influxdb_client.client.write_api import SYNCHRONOUS
    # Define where to write the data - must have set up DBRP for bucket
    bucket="L224"
    token = "RYKrniSyLGNxGSQA7TLnZSq6xydfANl8EnbgHzVLhLnpc5uD9zz82NZ7R_bEZYgeo0kq2C8aoWTOKU-hkM6B7w=="
    org = "PXS-Maggie"
    url = "http://localhost:8086"
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    # Convert value to string
    value_flt = float(value)
    units_str = str(units)

    # Create data point
    point = Point(loc).tag("source", machine).tag("channel", chan).field("test", value_flt)

    # Write data point to InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)