#!/usr/bin/env python
""" generated source for module for__0__COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDecodingDP(cls, digits, n):
        """ generated source for method countDecodingDP """
        count = [None]*n + 1
        count[0] = 1
        count[1] = 1
        if digits[0] == '0':
            return 0
        return count[n]

