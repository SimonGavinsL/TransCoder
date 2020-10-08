#!/usr/bin/env python
""" generated source for module for__1__LONGEST_COMMON_SUBSEQUENCE_WITH_PERMUTATIONS_ALLOWED """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestString(cls, str1, str2):
        """ generated source for method longestString """
        count1 = [None]*26
        count2 = [None]*26
        result = " "
        i = 0
        while i < 26:
            while j <= Math.min(count1[i], count2[i]):
                result += ((i))
                j += 1
            i += 1
        print result

