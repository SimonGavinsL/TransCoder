#!/usr/bin/env python
""" generated source for module for__0__FREQUENT_ELEMENT_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def mostFrequent(cls, arr, n):
        """ generated source for method mostFrequent """
        Arrays.sort(arr)
        max_count = 1
        res = arr[0]
        curr_count = 1
        if curr_count > max_count:
            max_count = curr_count
            res = arr[n - 1]
        return res

