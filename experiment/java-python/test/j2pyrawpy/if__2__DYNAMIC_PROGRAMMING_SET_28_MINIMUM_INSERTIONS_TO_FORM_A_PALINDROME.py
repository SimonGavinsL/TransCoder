#!/usr/bin/env python
""" generated source for module if__2__DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMinInsertions(cls, str_, l, h):
        """ generated source for method findMinInsertions """
        return cls.findMinInsertions(str_, l + 1, h - 1) if (str_[l] == str_[h]) else (Integer.min(cls.findMinInsertions(str_, l, h - 1), cls.findMinInsertions(str_, l + 1, h)) + 1)

