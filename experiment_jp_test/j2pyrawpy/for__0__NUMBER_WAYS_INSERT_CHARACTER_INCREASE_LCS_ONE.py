#!/usr/bin/env python
""" generated source for module for__0__NUMBER_WAYS_INSERT_CHARACTER_INCREASE_LCS_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberofways(cls, A, B, N, M):
        """ generated source for method numberofways """
        pos = [None]*MAX
        i = 0
        while i < M:
            i += 1
        dpl = [None]*N + 2
        i = 1
        while i <= N:
            while j <= M:
                if A.charAt(i - 1) == B.charAt(j - 1):
                    dpl[i][j] = dpl[i - 1][j - 1] + 1
                else:
                    dpl[i][j] = Math.max(dpl[i - 1][j], dpl[i][j - 1])
                j += 1
            i += 1
        LCS = dpl[N][M]
        dpr = [None]*N + 2
        i = N
        while i >= 1:
            while j >= 1:
                if A.charAt(i - 1) == B.charAt(j - 1):
                    dpr[i][j] = dpr[i + 1][j + 1] + 1
                else:
                    dpr[i][j] = Math.max(dpr[i + 1][j], dpr[i][j + 1])
                j -= 1
            i -= 1
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

