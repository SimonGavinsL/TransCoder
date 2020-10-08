#!/usr/bin/env python
""" generated source for module for__2__COUNT_NUMBER_WAYS_REACH_DESTINATION_MAZE """
class X(object):
    """ generated source for class X """
    @classmethod
    def countPaths(cls, maze):
        """ generated source for method countPaths """
        if maze[0][0] == -1:
            return 0
        return maze[R - 1][C - 1] if (maze[R - 1][C - 1] > 0) else 0

