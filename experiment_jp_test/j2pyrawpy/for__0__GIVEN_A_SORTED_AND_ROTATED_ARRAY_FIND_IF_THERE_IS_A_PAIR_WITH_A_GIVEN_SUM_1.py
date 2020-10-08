#!/usr/bin/env python
""" generated source for module for__0__GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def pairsInSortedRotated(cls, arr, n, x):
        """ generated source for method pairsInSortedRotated """
        i = int()
        l = (i + 1) % n
        r = i
        cnt = 0
        while l != r:
            if arr[l] + arr[r] == x:
                cnt += 1
                if l == (r - 1 + n) % n:
                    return cnt
                l = (l + 1) % n
                r = (r - 1 + n) % n
            elif arr[l] + arr[r] < x:
                l = (l + 1) % n
            else:
                r = (n + r - 1) % n
        return cnt

