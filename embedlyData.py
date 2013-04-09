
import pullEmbedly
import simplejson


def analyze(data):
	out = []
	data = pullEmbedly.get_oembed()
	
	for c in data:
		
		if c['urls'][0].has_key('oembed'):
			if c['urls'][0]['oembed'].has_key('title'):
				if c['urls'][0]['oembed'].has_key('description'):

					temp = dict();
					temp['ip'] = c['ip']
					temp['info'] = c['urls'][0]['oembed']['title']#+' '+c['urls'][0]['oembed']['description']
					out.append(temp)
		
		
	return out
	



