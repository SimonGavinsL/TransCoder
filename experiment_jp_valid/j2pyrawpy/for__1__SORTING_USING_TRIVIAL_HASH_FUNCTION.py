#!/usr/bin/env python
""" generated source for module for__1__SORTING_USING_TRIVIAL_HASH_FUNCTION """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortUsingHash(cls, a, n):
        """ generated source for method sortUsingHash """
        max = Arrays.stream(a).max().getAsInt()
        hash = [None]*max + 1

