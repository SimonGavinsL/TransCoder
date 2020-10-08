#!/usr/bin/env python
""" generated source for module if__0__FUNCTION_COPY_STRING_ITERATIVE_RECURSIVE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def myCopy(cls, s1, s2, index):
        """ generated source for method myCopy """
        s2[index] = s1[index]
        cls.myCopy(s1, s2, index + 1)

