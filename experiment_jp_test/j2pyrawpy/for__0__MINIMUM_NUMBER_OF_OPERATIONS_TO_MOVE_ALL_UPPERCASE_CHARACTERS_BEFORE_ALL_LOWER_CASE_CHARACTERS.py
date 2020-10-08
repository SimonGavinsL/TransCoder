#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_NUMBER_OF_OPERATIONS_TO_MOVE_ALL_UPPERCASE_CHARACTERS_BEFORE_ALL_LOWER_CASE_CHARACTERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def minOperations(cls, str_, n):
        """ generated source for method minOperations """
        i = int()
        lastUpper = -1
        firstLower = -1
        while i < n:
            if Character.isLowerCase(str_.charAt(i)):
                firstLower = i
                break
            i += 1
        if lastUpper == -1 or firstLower == -1:
            return 0
        countUpper = 0
        while i < n:
            if Character.isUpperCase(str_.charAt(i)):
                countUpper += 1
            i += 1
        countLower = 0
        while i < lastUpper:
            if Character.isLowerCase(str_.charAt(i)):
                countLower += 1
            i += 1
        return Math.min(countLower, countUpper)

