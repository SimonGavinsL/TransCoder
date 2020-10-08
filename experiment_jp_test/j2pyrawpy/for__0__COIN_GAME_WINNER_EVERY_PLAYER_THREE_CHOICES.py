#!/usr/bin/env python
""" generated source for module for__0__COIN_GAME_WINNER_EVERY_PLAYER_THREE_CHOICES """
class X(object):
    """ generated source for class X """
    @classmethod
    def findWinner(cls, x, y, n):
        """ generated source for method findWinner """
        dp = [None]*n + 1
        Arrays.fill(dp, False)
        dp[0] = False
        dp[1] = True
        return dp[n]

