#!/usr/bin/env python
import urllib
import urllib2
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Need a json decoder")

ACCEPTED_ARGS = ['maxwidth', 'maxheight', 'format']

def get_oembed( **kwargs):

    return json.loads(urllib2.urlopen("http://t.embed.ly/1/stream?key=pro").read())


