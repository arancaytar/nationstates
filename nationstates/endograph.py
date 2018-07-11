import numpy

class endograph:
    def __init__(self, s):
        nations, incoming, outgoing = set(), {}, {}
        edges = set(tuple(x.split(',')) for x in s.strip().split('\n'))
        for a, b in edges:
            nations.add(a)
            nations.add(b)
        for nation in nations:
            incoming[nation] = set()
            outgoing[nation] = set()
        for a, b in edges:
            outgoing[a].add(b)
            incoming[b].add(a)
        self.nations, self.edges, self.incoming, self.outgoing = nations, edges, incoming, outgoing

    def venn(self, nation, partition):
        if partition == 'neither':
            return self.nations.difference(self.incoming[nation]).difference(self.outgoing[nation])
        elif partition == 'incoming':
            return self.incoming[nation].difference(self.outgoing[nation])
        elif partition == 'outgoing':
            return self.outgoing[nation].difference(self.incoming[nation])
        elif partition == 'mutual':
            return self.outgoing[nation].intersection(self.incoming[nation])

    def prune(self, nation):
        return self.venn(nation, 'outgoing')

    def tart(self, nation):
        candidates = self.venn(nation, 'neither')
        data = lambda c:(
            len(self.venn(c, 'mutual')),
            len(self.incoming[c]),
            len(self.outgoing[c])
            )
        score = lambda z:(z[0]+0.01)**2/(z[1]+0.01)/(z[2]+0.01)
        result = []
        for c in candidates:
            x = data(c)
            result.append((c, x, score(x)))
        return sorted(result, key=lambda x:x[2], reverse=True)

    def matrix(self):
        M = numpy.zeros((len(self.nations), len(self.nations)))
        nkey = dict(zip(sorted(self.nations), range(len(self.nations))))
        for a,b in self.edges:
            M[nkey[a],nkey[b]] = 1
        return M


            
