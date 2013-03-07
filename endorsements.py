import ns
import argparse
import progress

def endorsements_region(region):
    nations = ns.region_shard(region, 'nations').find('NATIONS').text.split(':')
    edges = set()
    incoming = {}
    outgoing = {}
    for nation in progress.iterator(nations):
        given = ns.nation_shard(nation, 'endorsements').find('ENDORSEMENTS').text.split(',')
        for giver in given:
            edges.add((giver,nation))
        incoming[nation] = set(given)
        outgoing[nation] = set()
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
