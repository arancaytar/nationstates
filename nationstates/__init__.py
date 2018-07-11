import urllib3
import certifi
import xml.etree.ElementTree as xml
import os

from . import census
from . import throttle

ROOT = 'https://www.nationstates.net'
HTTP = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
THROTTLE = throttle.Throttler(30, 48)
HEADERS = {
  'User-agent': 'Ermarian (developer: +https://github.com/arancaytar/nationstates) (operator: {})'.format(
    os.environ.setdefault('NATIONSTATES_EMAIL', '-')
  )
}

def ns_api(fields):
    THROTTLE.wait()
    url = ROOT + '/cgi-bin/api.cgi?' + '&'.join(
            '{0}={1}'.format(a, b) for a,b in fields.items()
            )
    r = HTTP.request('GET', url, headers=HEADERS)
    if r.status == 421:
        raise ValueError("Scraper is currently blocked.")
    elif r.status == 404:
        raise ValueError("Requested entity does not exist.")
    elif r.status != 200:
        raise ValueError("Unknown error {}. Please visit {} for details.".format(r.status, url))
    THROTTLE.register()
    return xml.fromstring(r.data)

def nation_shard(nation, *shards):
    return ns_api({'nation' : nation, 'q' : '+'.join(shards)})

def nation_census(nation, *census_names):
    to_shard = lambda name: 'censusscore-{0}'.format(census.CENSUS_REVERSE[name])
    return nation_shard(nation, *map(to_shard, census_names)).find('CENSUSSCORE').text

def region_shard(region, *shards):
    return ns_api({'region' : region, 'q' : '+'.join(shards)})

def wa_shard(*shards, council_id=1):
    return ns_api({'wa' : council_id, 'q' : '+'.join(shards)})

def wa_members(region = None):
    members = wa_shard('members').find('MEMBERS').text.split(',')
    if region:
        residents = region_shard(region, 'nations').find('NATIONS').text.split(':')
        return set(members).intersection(residents)
    else:
        return set(members)


def loadxml(element):
    if len(element):
        data = {}
        for child in element:
            k = str(child.tag).lower()
            if 'type' in child.attrib:
                k = child.attrib['type']
            data[k] = loadxml(child)
        return data

    data = element.text

    if element.tag == 'ENDORSEMENTS':
        return data.split(',') if data else []
    elif element.tag == 'NATIONS':
        return data.split(':') # why.

    if element.tag == 'UNSTATUS':
        return data == 'WA Member'

    try:
        return int(data)
    except ValueError:
        pass

    try:
        return float(data)
    except ValueError:
        pass

    return data
