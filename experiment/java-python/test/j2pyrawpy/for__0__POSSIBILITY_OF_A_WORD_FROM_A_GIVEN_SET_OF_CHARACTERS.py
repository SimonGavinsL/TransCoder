#!/usr/bin/env python
""" generated source for module for__0__POSSIBILITY_OF_A_WORD_FROM_A_GIVEN_SET_OF_CHARACTERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPresent(cls, s, q):
        """ generated source for method isPresent """
        freq = [None]*MAX_CHAR
        i = 0
        while i < len(q):
            freq[q.charAt(i)] -= 1
            if freq[q.charAt(i)] < 0:
                return False
            i += 1
        return True

