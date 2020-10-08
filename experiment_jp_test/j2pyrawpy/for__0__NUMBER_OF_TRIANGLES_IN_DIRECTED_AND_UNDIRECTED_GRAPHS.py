#!/usr/bin/env python
""" generated source for module for__0__NUMBER_OF_TRIANGLES_IN_DIRECTED_AND_UNDIRECTED_GRAPHS """
class X(object):
    """ generated source for class X """
    def countTriangle(self, graph, isDirected):
        """ generated source for method countTriangle """
        count_Triangle = 0
        if isDirected == True:
            count_Triangle /= 3
        else:
            count_Triangle /= 6
        return count_Triangle

