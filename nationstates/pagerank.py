import numpy

def pagerank(M, d):
    A = numpy.eye(len(M))
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i,j]:
                A[i,j] -= d / sum(M[i,:])
    b = numpy.ones(len(M)) * (1-d) / len(M)
    return numpy.linalg.solve(A,b)

