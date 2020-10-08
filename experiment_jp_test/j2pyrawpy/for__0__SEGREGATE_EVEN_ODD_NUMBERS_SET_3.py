#!/usr/bin/env python
""" generated source for module for__0__SEGREGATE_EVEN_ODD_NUMBERS_SET_3 """
class X(object):
    """ generated source for class X """
    @classmethod
    def arrayEvenAndOdd(cls, arr, n):
        """ generated source for method arrayEvenAndOdd """
        i = -1
        j = 0
        while j != n:
            if arr[j] % 2 == 0:
                i += 1
                arr[i] = arr[j]
                arr[j] = temp
            j += 1

