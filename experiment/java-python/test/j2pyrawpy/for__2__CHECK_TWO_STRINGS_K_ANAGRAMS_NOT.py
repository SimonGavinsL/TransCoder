#!/usr/bin/env python
""" generated source for module for__2__CHECK_TWO_STRINGS_K_ANAGRAMS_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def arekAnagrams(cls, str1, str2, k):
        """ generated source for method arekAnagrams """
        n = len(str1)
        if len(str2) != n:
            return False
        count1 = [None]*MAX_CHAR
        count2 = [None]*MAX_CHAR
        count = 0
        return (count <= k)

