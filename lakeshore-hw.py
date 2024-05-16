# This scipt is a hello world tutorial for comms with lakeshore
from lakeshore import Model224

my_instrument = Model224()
#my_instrument.configure_input('C2',settings: sensor_type('diode'))
print(my_instrument.get_kelvin_reading('A'))