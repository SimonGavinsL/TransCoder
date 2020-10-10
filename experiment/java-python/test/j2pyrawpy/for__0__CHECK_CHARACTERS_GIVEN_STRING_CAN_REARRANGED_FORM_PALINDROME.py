#!/usr/bin/env python
""" generated source for module for__0__CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME """
class X(object):
    """ generated source for class X """
    @classmethod
    def canFormPalindrome(cls, str_):
        """ generated source for method canFormPalindrome """
        count = [None]*NO_OF_CHARS
        Arrays.fill(count, 0)
        odd = 0
        i = 0
        while i < NO_OF_CHARS:
            if (count[i] & 1) == 1:
                odd += 1
            if odd > 1:
                return False
            i += 1
        return True

