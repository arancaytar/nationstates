import endograph
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('nation', help='The name of the nation to help.')
    args = parser.parse_args()
    graph = endograph.endograph(sys.stdin.read())
    leeches = graph.prune(args.nation)
    print("\n".join(leeches))

main()
