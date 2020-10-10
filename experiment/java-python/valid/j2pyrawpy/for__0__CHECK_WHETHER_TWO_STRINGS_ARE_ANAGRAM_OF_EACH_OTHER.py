#!/usr/bin/env python
""" generated source for module for__0__CHECK_WHETHER_TWO_STRINGS_ARE_ANAGRAM_OF_EACH_OTHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def areAnagram(cls, str1, str2):
        """ generated source for method areAnagram """
        n1 = str1.length
        n2 = str2.length
        if n1 != n2:
            return False
        Arrays.sort(str1)
        Arrays.sort(str2)
        return True

