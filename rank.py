import endograph
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    graph = endograph.endograph(sys.stdin.read())
    rank = sorted(sorted(graph.nations), key=lambda n:len(graph.incoming[n]), reverse=True)
    n = max(map(len, graph.nations))
    m = max(map(len, map(str, map(len, graph.incoming.values()))))
    k = max(map(len, map(str, map(len, graph.outgoing.values()))))
    for i,nation in enumerate(rank):
        print("{{n}}\t{{name: <{0}s}}\t{{inc: {1}}}\t{{out: {2}}}".format(n,m,k).format(n=i+1, name=nation, inc=len(graph.incoming[nation]), out=len(graph.outgoing[nation])))

main()
