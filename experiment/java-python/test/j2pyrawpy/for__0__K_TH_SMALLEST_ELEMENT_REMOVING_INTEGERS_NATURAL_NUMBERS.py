#!/usr/bin/env python
""" generated source for module for__0__K_TH_SMALLEST_ELEMENT_REMOVING_INTEGERS_NATURAL_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def ksmallest(cls, arr, n, k):
        """ generated source for method ksmallest """
        b = [None]*MAX
        j = 1
        while j < MAX:
            if b[j] != 1:
                k -= 1
            if k != 1:
                return j
            j += 1
        return Integer.MAX_VALUE

