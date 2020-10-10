#!/usr/bin/env python
""" generated source for module for__0__DISCRETE_LOGARITHM_FIND_INTEGER_K_AK_CONGRUENT_MODULO_B """
class X(object):
    """ generated source for class X """
    @classmethod
    def discreteLogarithm(cls, a, b, m):
        """ generated source for method discreteLogarithm """
        n = ((Math.sqrt(m) + 1))
        an = 1
        value = [None]*m
        i = 1
        cur = an
        while i <= n:
            if value[cur] == 0:
                value[cur] = i
            cur = (cur * an) % m
            i += 1
        i = 0
        cur = b
        while i <= n:
            if value[cur] > 0:
                if ans < m:
                    return ans
            cur = (cur * a) % m
            i += 1
        return -1

