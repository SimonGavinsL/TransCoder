#!/usr/bin/env python
""" generated source for module if__0__SHORTEST_PATH_EXACTLY_K_EDGES_DIRECTED_WEIGHTED_GRAPH """
class X(object):
    """ generated source for class X """
    def shortestPath(self, graph, u, v, k):
        """ generated source for method shortestPath """
        if k == 1 and graph[u][v] != INF:
            return graph[u][v]
        if k <= 0:
            return INF
        res = INF
        return res

