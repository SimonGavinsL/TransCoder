#!/usr/bin/env python
""" generated source for module for__0__COUNT_POSSIBLE_WAYS_TO_CONSTRUCT_BUILDINGS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWays(cls, N):
        """ generated source for method countWays """
        if N == 1:
            return 4
        countB = 1
        countS = 1
        prev_countB = int()
        prev_countS = int()
        result = countS + countB
        return (result * result)

