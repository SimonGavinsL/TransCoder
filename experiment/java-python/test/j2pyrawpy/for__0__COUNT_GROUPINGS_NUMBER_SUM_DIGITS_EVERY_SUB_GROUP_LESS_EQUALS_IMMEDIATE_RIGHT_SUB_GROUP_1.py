#!/usr/bin/env python
""" generated source for module for__0__COUNT_GROUPINGS_NUMBER_SUM_DIGITS_EVERY_SUB_GROUP_LESS_EQUALS_IMMEDIATE_RIGHT_SUB_GROUP_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countGroups(cls, position, previous_sum, length, num):
        """ generated source for method countGroups """
        if position == length:
            return 1
        if dp[position][previous_sum] != -1:
            return dp[position][previous_sum]
        dp[position][previous_sum] = 0
        res = 0
        sum = 0
        dp[position][previous_sum] = res
        return res

