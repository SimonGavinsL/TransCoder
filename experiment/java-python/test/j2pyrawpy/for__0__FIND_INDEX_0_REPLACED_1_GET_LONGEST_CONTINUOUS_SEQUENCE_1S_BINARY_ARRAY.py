#!/usr/bin/env python
""" generated source for module for__0__FIND_INDEX_0_REPLACED_1_GET_LONGEST_CONTINUOUS_SEQUENCE_1S_BINARY_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxOnesIndex(cls, arr, n):
        """ generated source for method maxOnesIndex """
        max_count = 0
        max_index = 0
        prev_zero = -1
        prev_prev_zero = -1
        if n - prev_prev_zero > max_count:
            max_index = prev_zero
        return max_index

