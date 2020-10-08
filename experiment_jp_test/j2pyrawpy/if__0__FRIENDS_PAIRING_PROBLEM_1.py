#!/usr/bin/env python
""" generated source for module if__0__FRIENDS_PAIRING_PROBLEM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countFriendsPairings(cls, n):
        """ generated source for method countFriendsPairings """
        if n > 2:
            return dp[n] = countFriendsPairings(n - 1) + (n - 1) * countFriendsPairings(n - 2)
        else:
            return dp[n] = n

