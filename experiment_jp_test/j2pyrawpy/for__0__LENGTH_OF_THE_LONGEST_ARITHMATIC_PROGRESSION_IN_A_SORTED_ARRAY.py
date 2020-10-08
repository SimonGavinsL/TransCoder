#!/usr/bin/env python
""" generated source for module for__0__LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def lenghtOfLongestAP(cls, set, n):
        """ generated source for method lenghtOfLongestAP """
        if n <= 2:
            return n
        L = [None]*n
        llap = 2
        j = n - 2
        while j >= 1:
            while i >= 0 and k <= n - 1:
                if set[i] + set[k] < 2 * set[j]:
                    k += 1
                elif set[i] + set[k] > 2 * set[j]:
                    L[i][j] = 2
                    i -= 1
                else:
                    L[i][j] = L[j][k] + 1
                    llap = Math.max(llap, L[i][j])
                    i -= 1
                    k += 1
            while i >= 0:
                L[i][j] = 2
                i -= 1
            j -= 1
        return llap

