#!/usr/bin/env python
""" generated source for module if__0__NUMBER_WAYS_NODE_MAKE_LOOP_SIZE_K_UNDIRECTED_COMPLETE_CONNECTED_GRAPH_N_NODES """
class X(object):
    """ generated source for class X """
    @classmethod
    def numOfways(cls, n, k):
        """ generated source for method numOfways """
        p = 1
        return ((Math.pow(n - 1, k) + p * (n - 1))) / n

