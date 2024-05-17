""" string = "Hello World!"
pp = 0
for x in range(0,3):
	print(pp)
	pp += 1 """

from maggie_functions import ky
KY_channels = ["CH1","CH2","CH3"]
for x in KY_channels:
	print(float(ky('current',x)))