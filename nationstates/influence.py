import ns
import argparse
import progress

def influence_region(region):
    nations = ns.region_shard(region, 'nations').find('NATIONS').text.split(':')
    scores = {}
    for nation in progress.iterator(nations):
        scores[nation] = int(ns.nation_census(nation, 'influence'))
    return scores

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('region', help='The name of the region to survey.')
    args = parser.parse_args()
    scores = influence_region(args.region)
    nations = sorted(scores.keys())
    nations.sort(key=lambda s:scores[s], reverse=True)
    print("\n".join("{0},{1}".format(n, scores[n]) for n in nations))

main()
