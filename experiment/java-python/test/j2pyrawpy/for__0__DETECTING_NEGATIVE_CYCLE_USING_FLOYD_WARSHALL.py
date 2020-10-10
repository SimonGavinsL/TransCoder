#!/usr/bin/env python
""" generated source for module for__0__DETECTING_NEGATIVE_CYCLE_USING_FLOYD_WARSHALL """
class X(object):
    """ generated source for class X """
    @classmethod
    def negCyclefloydWarshall(cls, graph):
        """ generated source for method negCyclefloydWarshall """
        dist = [None]*V
        i = int()
        j = int()
        k = int()
        while k < V:
            while i < V:
                while j < V:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                    j += 1
                i += 1
            k += 1
        while i < V:
            i += 1
        return False

