#!/usr/bin/env python
""" generated source for module for__0__COUNT_ARITHMETIC_PROGRESSION_SUBSEQUENCES_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def numofAP(cls, a, n):
        """ generated source for method numofAP """
        minarr = +2147483647
        maxarr = -2147483648
        dp = [None]*n
        sum = [None]*MAX
        ans = n + 1
        d = (minarr - maxarr)
        while d <= (maxarr - minarr):
            Arrays.fill(sum, 0)
            while i < n:
                dp[i] = 1
                if a[i] - d >= 1 and a[i] - d <= 1000000:
                    dp[i] += sum[a[i] - d]
                ans += dp[i] - 1
                sum[a[i]] += dp[i]
                i += 1
            d += 1
        return ans

