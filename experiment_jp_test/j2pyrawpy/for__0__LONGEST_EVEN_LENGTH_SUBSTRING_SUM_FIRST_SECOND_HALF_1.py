#!/usr/bin/env python
""" generated source for module for__0__LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLength(cls, str_):
        """ generated source for method findLength """
        n = len(str_)
        maxlen = 0
        sum = [None]*n
        len = 2
        while len <= n:
            while i < n - len + 1:
                sum[i][j] = sum[i][j - k] + sum[j - k + 1][j]
                if len % 2 == 0 and sum[i][j - k] == sum[(j - k + 1)][j] and len > maxlen:
                    maxlen = len
                i += 1
            len += 1
        return maxlen

