import endograph
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('nation', help='The name of the nation to help.')
    args = parser.parse_args()
    graph = endograph.endograph(sys.stdin.read())
    scores = graph.tart(args.nation)
    print('''
<!DOCTYPE html>
<html>
  <head>
    <title>Tarting for {nation}</title>
  </head>
  <body>
    <table>{text}</table>
  </body>
</html>'''.format(nation=args.nation, text=''.join(
        '''
<tr>
  <td><a href="http://www.nationstates.net/{nation}">{nation}</a></td>
  <td>{score:.3f}</td>
  <td>{mutual}</td>
  <td>{incoming}</td>
  <td>{outgoing}</td>
</tr>'''.format(nation=nation,mutual=mutual,incoming=incoming,outgoing=outgoing,score=score) for nation,(mutual,incoming,outgoing),score in scores)))

main()
