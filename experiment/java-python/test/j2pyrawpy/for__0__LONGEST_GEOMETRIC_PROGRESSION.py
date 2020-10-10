#!/usr/bin/env python
""" generated source for module for__0__LONGEST_GEOMETRIC_PROGRESSION """
class X(object):
    """ generated source for class X """
    @classmethod
    def lenOfLongestGP(cls, set, n):
        """ generated source for method lenOfLongestGP """
        if n < 2:
            return n
        if n == 2:
            return (1 if set[1] % set[0] == 0 else 0)
        Arrays.sort(set)
        L = [None]*n
        llgp = 1
        j = n - 2
        while j >= 1:
            while i >= 0 and k <= n - 1:
                if set[i] * set[k] < set[j] * set[j]:
                    k += 1
                elif set[i] * set[k] > set[j] * set[j]:
                    if set[j] % set[i] == 0:
                        L[i][j] = 2
                    else:
                        L[i][j] = 1
                    i -= 1
                else:
                    L[i][j] = L[j][k] + 1
                    if L[i][j] > llgp:
                        llgp = L[i][j]
                    i -= 1
                    k += 1
            while i >= 0:
                if set[j] % set[i] == 0:
                    L[i][j] = 2
                else:
                    L[i][j] = 1
                i -= 1
            j -= 1
        return llgp

