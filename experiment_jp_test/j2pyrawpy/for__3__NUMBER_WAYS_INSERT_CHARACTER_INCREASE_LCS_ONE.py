#!/usr/bin/env python
""" generated source for module for__3__NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberofways(cls, A, B, N, M):
        """ generated source for method numberofways """
        pos = [None]*MAX
        dpl = [None]*N + 2
        LCS = dpl[N][M]
        dpr = [None]*N + 2
        ans = 0
        i = 0
        while i <= N:
            while j < MAX:
                for x in pos[j]:
                    if dpl[i][x - 1] + dpr[i + 1][x + 1] == LCS:
                        ans += 1
                        break
                j += 1
            i += 1
        return ans

