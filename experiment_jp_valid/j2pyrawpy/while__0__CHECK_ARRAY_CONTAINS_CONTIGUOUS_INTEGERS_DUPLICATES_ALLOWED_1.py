#!/usr/bin/env python
""" generated source for module while__0__CHECK_ARRAY_CONTAINS_CONTIGUOUS_INTEGERS_DUPLICATES_ALLOWED_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def areElementsContiguous(cls, arr, n):
        """ generated source for method areElementsContiguous """
        us = HashSet()
        count = 1
        curr_ele = arr[0] - 1
        curr_ele = arr[0] + 1
        while us.contains(curr_ele) == True:
            count += 1
            curr_ele += 1
        return (count == (len(us)))

