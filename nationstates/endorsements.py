import ns
import argparse
import progress

def endorsements_region(region):
    edges = set()
    incoming = {}
    outgoing = {}
    for nation in progress.iterator(ns.wa_members(region)):
        outgoing[nation] = set()
        incoming[nation] = set()
        given = ns.nation_shard(nation, 'endorsements').find('ENDORSEMENTS')
        if not given.text:
            continue
        given = given.text.split(',')
        for giver in given:
            edges.add((giver,nation))
        incoming[nation] = set(given)
    for giver,receiver in edges:
        outgoing[giver].add(receiver)
    return incoming,outgoing,edges

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('region', help='The name of the region to survey.')
    args = parser.parse_args()
    _,_,edges = endorsements_region(args.region)
    print("\n".join("{0},{1}".format(a,b) for a,b in edges))

main()
