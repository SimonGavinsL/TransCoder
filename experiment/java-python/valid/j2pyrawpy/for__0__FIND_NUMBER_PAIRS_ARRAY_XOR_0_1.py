#!/usr/bin/env python
""" generated source for module for__0__FIND_NUMBER_PAIRS_ARRAY_XOR_0_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def calculate(cls, a, n):
        """ generated source for method calculate """
        maximum = Arrays.stream(a).max().getAsInt()
        frequency = [None]*maximum + 1
        answer = 0
        i = 0
        while i < maximum(+1):
            answer = answer + frequency[i] * (frequency[i] - 1)
            i += 1
        return answer / 2

