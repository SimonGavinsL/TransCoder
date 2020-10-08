#!/usr/bin/env python
""" generated source for module for__0__COUNT_POSSIBLE_PATHS_SOURCE_DESTINATION_EXACTLY_K_EDGES """
class X(object):
    """ generated source for class X """
    def countwalks(self, graph, u, v, k):
        """ generated source for method countwalks """
        if k == 0 and u == v:
            return 1
        if k == 1 and graph[u][v] == 1:
            return 1
        if k <= 0:
            return 0
        count = 0
        return count

