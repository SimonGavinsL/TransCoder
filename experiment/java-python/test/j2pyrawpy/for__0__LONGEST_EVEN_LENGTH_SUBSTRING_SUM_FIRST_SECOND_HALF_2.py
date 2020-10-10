#!/usr/bin/env python
""" generated source for module for__0__LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLength(cls, str_, n):
        """ generated source for method findLength """
        sum = [None]*n + 1
        sum[0] = 0
        ans = 0
        len = 2
        while len <= n:
            while i <= n - len:
                if sum[i + len / 2] - sum[i] == sum[i + len] - sum[i + len / 2]:
                    ans = Math.max(ans, len)
                i += 1
            len += 2
        return ans

