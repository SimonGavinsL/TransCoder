#!/usr/bin/env python
""" generated source for module for__0__K_MAXIMUM_SUM_COMBINATIONS_TWO_ARRAYS """
class X(object):
    """ generated source for class X """
    @classmethod
    def KMaxCombinations(cls, A, B, N, K):
        """ generated source for method KMaxCombinations """
        pq = PriorityQueue(Collections.reverseOrder())
        count = 0
        while count < K:
            print pq.peek()
            pq.remove()
            count += 1

