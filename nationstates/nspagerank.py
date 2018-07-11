import argparse
import endograph
import pagerank
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('damping', nargs='?', help='The damping factor to use.', type=int, default=0.85)
    args = parser.parse_args()
    graph = endograph.endograph(sys.stdin.read())
    scores = zip(sorted(graph.nations), pagerank.pagerank(graph.matrix(), args.damping))
    print("\n".join(
        "%.10f %s" % (b,a) for (a,b) in 
        sorted(scores, key=lambda z:z[1], reverse=True)
        ))


    
main()
