#!/usr/bin/env python3

import ns
import argparse
import json
import yaml

parser = argparse.ArgumentParser(description='Access the NS API.')

parser.add_argument('type', type=str, help='Either "nation" or "region".')
parser.add_argument('name', type=str, help='Name of nation or region.')
parser.add_argument('shards', type=str, nargs='*', help='Shards to query.', default=[])
parser.add_argument('--format', type=str, help='Format (json, yaml, txt). Defaults to txt for single scalar values, json otherwise.', default='txt')
args = parser.parse_args()
if args.type == 'region':
    method = ns.region_shard
elif args.type == 'nation':
    method = ns.nation_shard
else:
    raise ValueError('Type must be "nation" or "region".')

if args.format not in ('txt', 'json', 'yaml'):
    raise ValueError('Format must be txt, json or yaml.')

data = ns.loadxml(method(args.name, *args.shards))

if args.format == 'txt' and (len(data) > 1 or type(list(data.values())[0]) in (dict, list)):
    args.format = 'json'

if args.format == 'txt':
    print(list(data.values())[0])
elif args.format == 'json':
    print(json.dumps(data, indent=4))
elif args.format == 'yaml':
    print(yaml.dump(data, indent=4, default_flow_style=False))

