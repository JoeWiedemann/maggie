# Master Data aqusition and write function

import maggie_functions as mf

L224_channels = ["CHA","CHB","CHC1", "CHC2", "CHC3", "CHC4"]
KY_channels = ["CH1","CH2","CH3"]

loc = "test_16May"

def getdata():
    for ky_chan in KY_channels:
        mf.idb(loc, "Keithley", ky_chan, "Amps", mf.ky("amps", ky_chan))
        mf.idb(loc, "Keithley", ky_chan, "Volts", mf.ky("volterinos", ky_chan))
    for L_chan in L224_channels:
        mf.idb(loc, "L224", L_chan, "Kelvin", mf.ls224("kelvin", L_chan))
        mf.idb(loc, "L224", L_chan, "Voltage", mf.ls224("voltage", L_chan))


while(1):
	getdata()