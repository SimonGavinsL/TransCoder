#!/usr/bin/env python
""" generated source for module for__2__SORTING_USING_TRIVIAL_HASH_FUNCTION_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortUsingHash(cls, a, n):
        """ generated source for method sortUsingHash """
        max = Arrays.stream(a).max().getAsInt()
        min = Math.abs(Arrays.stream(a).min().getAsInt())
        hashpos = [None]*max + 1
        hashneg = [None]*min + 1

