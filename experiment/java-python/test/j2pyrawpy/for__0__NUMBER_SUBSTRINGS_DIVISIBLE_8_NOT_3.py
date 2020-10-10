#!/usr/bin/env python
""" generated source for module for__0__NUMBER_SUBSTRINGS_DIVISIBLE_8_NOT_3 """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, s, len):
        """ generated source for method count """
        MAX = 1000
        cur = 0
        dig = 0
        sum = [None]*MAX
        dp = [None]*MAX
        dp[0][0] = 1
        ans = 0
        dprev = 0
        value = 0
        dprev2 = 0
        i = 1
        while i <= len:
            dig = ((s.charAt(i - 1))) - 48
            if dig == 8:
                ans += 1
            if i - 2 >= 0:
                dprev = ((s.charAt(i - 2))) - 48
                value = dprev * 10 + dig
                if (value % 8 == 0) and (value % 3 != 0):
                    ans += 1
            if i - 3 >= 0:
                dprev2 = ((s.charAt(i - 3))) - 48
                dprev = ((s.charAt(i - 2))) - 48
                value = dprev2 * 100 + dprev * 10 + dig
                if value % 8 != 0:
                    continue 
                ans += (i - 2)
                ans -= (dp[i - 3][sum[i]])
            i += 1
        return ans

