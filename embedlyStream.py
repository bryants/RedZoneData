import time
import httplib2
from datetime import datetime
import urllib
import urllib2
from pullEmbedly import *
from embedlyData import *
from getloc import *
from pullGS import *



clock0 = time.clock()
clock1 = time.clock()
while 1:
	
	if clock1> clock0+1:
		clock0 = time.clock()
		f=get_oembed()
		data = analyze(f)
		for c in data:

			loc= getLocation(c['ip'])
			c['lat'] = loc['Latitude']
			c['long'] = loc['Longitude']
			c['word'] = c['info']
			date = datetime.today().isoformat()[0:10].replace('-','')
			print date
			gs = pullGS(date,date,c['word'])
			print gs
			time.sleep(3)
			
			
	clock1 = time.clock()

		

	
