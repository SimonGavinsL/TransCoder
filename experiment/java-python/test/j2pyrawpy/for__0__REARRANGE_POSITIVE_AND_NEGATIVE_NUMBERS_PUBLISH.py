#!/usr/bin/env python
""" generated source for module for__0__REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH """
class X(object):
    """ generated source for class X """
    @classmethod
    def rearrange(cls, arr, n):
        """ generated source for method rearrange """
        i = -1
        temp = 0
        pos = i + 1
        neg = 0
        while pos < n and neg < pos and arr[neg] < 0:
            temp = arr[neg]
            arr[neg] = arr[pos]
            arr[pos] = temp
            pos += 1
            neg += 2

