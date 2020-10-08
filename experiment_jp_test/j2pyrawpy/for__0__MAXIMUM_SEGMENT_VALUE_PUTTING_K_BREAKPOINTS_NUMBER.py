#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SEGMENT_VALUE_PUTTING_K_BREAKPOINTS_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxSegment(cls, s, k):
        """ generated source for method findMaxSegment """
        seg_len = len(s) - k
        res = 0
        seg_len_pow = (Math.pow(10, seg_len - 1))
        curr_val = res
        i = 1
        while i <= len((s) - seg_len):
            curr_val = curr_val - (s.charAt(i - 1) - '0') * seg_len_pow
            curr_val = curr_val * 10 + (s.charAt(i + seg_len - 1) - '0')
            res = Math.max(res, curr_val)
            i += 1
        return res

