# Hello world script to communicate with Keithly which requires SCPI

""" import pyvisa
import time

# This is port, manufactuer ID, Device ID, Serial Number from dmesg
A = pyvisa.instrument("USB0::0x05E6::0x2230::9210309::INSTR")

A.write("system:remote")
A.write("*IDN?") """

import pyvisa

rm = pyvisa.ResourceManager()

# print(rm.list_resources())
#('ASRL/dev/ttyS5::INSTR', 'ASRL/dev/ttyS4::INSTR', 'ASRL/dev/ttyS0::INSTR', 'ASRL/dev/ttyUSB0::INSTR')

inst = rm.open_resource('USB0::1510::8752::9210309::0::INSTR')

#print(inst.write("SYST:REM"))

field = 'current'
chan = 'CH1'
s1 = 'fetch:'
s2 = '? '

print(inst.query(s1+field+s2+chan))
#print(inst.query("fetch:current? CH1"))