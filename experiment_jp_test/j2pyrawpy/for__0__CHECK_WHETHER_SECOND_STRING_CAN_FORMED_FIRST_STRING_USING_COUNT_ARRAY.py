#!/usr/bin/env python
""" generated source for module for__0__CHECK_WHETHER_SECOND_STRING_CAN_FORMED_FIRST_STRING_USING_COUNT_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def canMakeStr2(cls, str1, str2):
        """ generated source for method canMakeStr2 """
        count = [None]*MAX
        str3 = str1.toCharArray()
        str4 = str2.toCharArray()
        i = 0
        while i < str4.length:
            if count[str4[i]] == 0:
                return False
            count[str4[i]] -= 1
            i += 1
        return True

