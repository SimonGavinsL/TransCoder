#!/usr/bin/env python
""" generated source for module for__0__FREQUENCY_ELEMENT_UNSORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countFreq(cls, a, n):
        """ generated source for method countFreq """
        hm = [None]*n
        cumul = 0
        i = 0
        while i < n:
            cumul += hm[a[i]]
            if hm[a[i]] != 0:
                print a[i] + " - > " + cumul
            hm[a[i]] = 0
            i += 1

