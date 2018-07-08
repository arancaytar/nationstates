import urllib3
import certifi
import xml.etree.ElementTree as xml
import throttle
import os

ROOT = 'https://www.nationstates.net'
HTTP = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
__DIR__ = os.path.dirname(__file__)
CENSUS = dict(map(lambda z:(z[1], int(z[0])), (s.split("\t") for s in open(__DIR__ + '/censusscore.txt').read().strip().split("\n"))))
THROTTLE = throttle.Throttler(30, 48)
try:
    EMAIL = open(__DIR__ + '/email.txt').read().strip()
except IOError:
    EMAIL = ''
HEADERS = {
  'User-agent': 'Ermarian (developer: +https://github.com/cburschka/nationstates) (operator: {})'.format(EMAIL)
}

def ns_api(fields):
    THROTTLE.wait()
    url = ROOT + '/cgi-bin/api.cgi?' + '&'.join(
            '{0}={1}'.format(a, b) for a,b in fields.items()
            )
    r = HTTP.request('GET', url, headers=HEADERS)
    if r.status == 421:
        raise ValueError("Scraper is currently blocked.")
    elif r.status != 200:
        raise ValueError("Unknown error. Please visit {0} for details.".format(url))
    THROTTLE.register()
    return xml.fromstring(r.data)

def nation_shard(nation, shard):
    return ns_api({'nation' : nation, 'q' : shard})

def nation_census(nation, census_name):
    return nation_shard(nation, 'censusscore-{0}'.format(CENSUS[census_name])).find('CENSUSSCORE').text

def region_shard(region, shard):
    return ns_api({'region' : region, 'q' : shard})

def wa_shard(shard, wa=1):
    return ns_api({'wa' : wa, 'q' : shard})

def wa_members(region = None):
    members = wa_shard('members').find('MEMBERS').text.split(',')
    if region:
        residents = region_shard(region, 'nations').find('NATIONS').text.split(':')
        return set(members).intersection(residents)
    else:
        return set(members)

