#!/usr/bin/env python
""" generated source for module for__0__CHECK_CHARACTERS_GIVEN_STRING_CAN_REARRANGED_FORM_PALINDROME_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def canFormPalindrome(cls, str_):
        """ generated source for method canFormPalindrome """
        list_ = ArrayList()
        if len(str_) % 2 == 0 and list_.isEmpty() or len((str_) % 2 == 1 and len(list_) == 1):
            return True
        else:
            return False

