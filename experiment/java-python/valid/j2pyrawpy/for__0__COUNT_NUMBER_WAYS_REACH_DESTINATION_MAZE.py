#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_WAYS_REACH_DESTINATION_MAZE """
class X(object):
    """ generated source for class X """
    @classmethod
    def countPaths(cls, maze):
        """ generated source for method countPaths """
        if maze[0][0] == -1:
            return 0
        i = 1
        while i < C:
            if maze[0][i] == 0:
                maze[0][i] = 1
            else:
                break
            i += 1
        i = 1
        while i < R:
            while j < C:
                if maze[i][j] == -1:
                    continue 
                if maze[i - 1][j] > 0:
                    maze[i][j] = (maze[i][j] + maze[i - 1][j])
                if maze[i][j - 1] > 0:
                    maze[i][j] = (maze[i][j] + maze[i][j - 1])
                j += 1
            i += 1
        return maze[R - 1][C - 1] if (maze[R - 1][C - 1] > 0) else 0

