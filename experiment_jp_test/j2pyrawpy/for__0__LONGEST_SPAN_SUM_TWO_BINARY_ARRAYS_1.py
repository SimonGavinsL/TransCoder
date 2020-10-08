#!/usr/bin/env python
""" generated source for module for__0__LONGEST_SPAN_SUM_TWO_BINARY_ARRAYS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestCommonSum(cls, n):
        """ generated source for method longestCommonSum """
        maxLen = 0
        preSum1 = 0
        preSum2 = 0
        diff = [None]*2 * n + 1
        i = 0
        while i < n:
            preSum1 += arr1[i]
            preSum2 += arr2[i]
            if curr_diff == 0:
                maxLen = i + 1
            elif diff[diffIndex] == -1:
                diff[diffIndex] = i
            else:
                if len > maxLen:
                    maxLen = len
            i += 1
        return maxLen

