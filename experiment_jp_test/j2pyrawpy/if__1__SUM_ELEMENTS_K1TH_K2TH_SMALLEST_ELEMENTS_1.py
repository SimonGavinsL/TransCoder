#!/usr/bin/env python
""" generated source for module if__1__SUM_ELEMENTS_K1TH_K2TH_SMALLEST_ELEMENTS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minheapify(cls, a, index):
        """ generated source for method minheapify """
        small = index
        l = 2 * index + 1
        r = 2 * index + 2
        if small != index:
            a[small] = a[index]
            a[index] = t
            cls.minheapify(a, small)

