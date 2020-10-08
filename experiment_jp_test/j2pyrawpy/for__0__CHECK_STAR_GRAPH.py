#!/usr/bin/env python
""" generated source for module for__0__CHECK_STAR_GRAPH """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkStar(cls, mat):
        """ generated source for method checkStar """
        vertexD1 = 0
        vertexDn_1 = 0
        if size == 1:
            return (mat[0][0] == 0)
        if size == 2:
            return (mat[0][0] == 0 and mat[0][1] == 1 and mat[1][0] == 1 and mat[1][1] == 0)
        return (vertexD1 == (size - 1) and vertexDn_1 == 1)

