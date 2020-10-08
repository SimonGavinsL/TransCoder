#!/usr/bin/env python
""" generated source for module for__0__SUBSEQUENCES_SIZE_THREE_ARRAY_WHOSE_SUM_DIVISIBLE_M_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSubSeq(cls, A, N, M):
        """ generated source for method countSubSeq """
        ans = 0
        h = [None]*M
        Arrays.fill(h, 0)
        i = 0
        while i < M:
            while j < M:
                if rem < j:
                    continue 
                if i == j and rem == j:
                    ans += h[i] * (h[i] - 1) * (h[i] - 2) / 6
                elif i == j:
                    ans += h[i] * (h[i] - 1) * h[rem] / 2
                elif i == rem:
                    ans += h[i] * (h[i] - 1) * h[j] / 2
                elif rem == j:
                    ans += h[j] * (h[j] - 1) * h[i] / 2
                else:
                    ans = ans + h[i] * h[j] * h[rem]
                j += 1
            i += 1
        return ans

