# Master Fucntions File

# For Power supply, field and chan must be strings 
# field can be current or voltage. chan can be ch1 ch2 ch3
def keithley(field,chan):
    import pyvisa
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('USB0::1510::8752::9210309::0::INSTR') # this is serial number specific
    s1 = 'fetch:'
    s2 = '? '
    
    return(inst.query(s1+field+s2+chan))

