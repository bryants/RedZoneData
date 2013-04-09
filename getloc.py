
from IPInfo import *
import simplejson
 
 #a = IPInfo('c1a21e781de72cdf25a0ff3472054f3021540c255199a992f3f7773e9fe46536')
'''
a = IPInfo('c1a21e781de72cdf25a0ff3472054f3021540c255199a992f3f7773e9fe46536')
output = a.GetCity('128.6.13.155')
print output['RegionName']
print simplejson.dumps(output, sort_keys=True, indent=4)
'''

def getLocation(ipAddress):
	a = IPInfo('c1a21e781de72cdf25a0ff3472054f3021540c255199a992f3f7773e9fe46536')
	output = a.GetCity(ipAddress)
	return output

