#!/usr/bin/env python
""" generated source for module if__3__LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED """
class X(object):
    """ generated source for class X """
    @classmethod
    def lcs(cls, dp, arr1, n, arr2, m, k):
        """ generated source for method lcs """
        ans = dp[n][m][k]
        try:
            ans = Math.max(lcs(dp, arr1, n - 1, arr2, m, k), lcs(dp, arr1, n, arr2, m - 1, k))
            ans = Math.max(ans, 1 + lcs(dp, arr1, n - 1, arr2, m - 1, k - 1))
        except Exception as e:
            pass
        return ans

