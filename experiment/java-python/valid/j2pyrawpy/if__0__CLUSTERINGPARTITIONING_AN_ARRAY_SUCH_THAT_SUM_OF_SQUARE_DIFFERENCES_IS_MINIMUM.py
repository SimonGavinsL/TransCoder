#!/usr/bin/env python
""" generated source for module if__0__CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM """
class X(object):
    """ generated source for class X """
    @classmethod
    def solve(cls, i, par, a, n, k, current_ans):
        """ generated source for method solve """
        if par == k and i == n - 1:
            ans = Math.min(ans, current_ans)
            return

