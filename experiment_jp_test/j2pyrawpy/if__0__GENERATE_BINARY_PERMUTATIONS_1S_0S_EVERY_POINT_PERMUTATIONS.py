#!/usr/bin/env python
""" generated source for module if__0__GENERATE_BINARY_PERMUTATIONS_1S_0S_EVERY_POINT_PERMUTATIONS """
class X(object):
    """ generated source for class X """
    @classmethod
    def generate(cls, ones, zeroes, str_, len):
        """ generated source for method generate """
        cls.generate(ones + 1, zeroes, str_ + "1", len)
        if ones > zeroes:
            cls.generate(ones, zeroes + 1, str_ + "0", len)

