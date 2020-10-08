#!/usr/bin/env python
""" generated source for module for__0__GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM """
class X(object):
    """ generated source for class X """
    @classmethod
    def pairInSortedRotated(cls, arr, n, x):
        """ generated source for method pairInSortedRotated """
        i = int()
        l = (i + 1) % n
        r = i
        while l != r:
            if arr[l] + arr[r] == x:
                return True
            if arr[l] + arr[r] < x:
                l = (l + 1) % n
            else:
                r = (n + r - 1) % n
        return False

