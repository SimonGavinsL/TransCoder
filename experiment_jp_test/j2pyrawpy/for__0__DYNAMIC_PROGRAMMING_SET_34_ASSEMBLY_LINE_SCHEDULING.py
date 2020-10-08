#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_34_ASSEMBLY_LINE_SCHEDULING """
class X(object):
    """ generated source for class X """
    @classmethod
    def carAssembly(cls, a, t, e, x):
        """ generated source for method carAssembly """
        T1 = [None]*NUM_STATION
        T2 = [None]*NUM_STATION
        i = int()
        T1[0] = e[0] + a[0][0]
        T2[0] = e[1] + a[1][0]
        return min(T1[NUM_STATION - 1] + x[0], T2[NUM_STATION - 1] + x[1])

