#!/usr/bin/env python
""" generated source for module for__0__FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS_1 """
class X(object):
    """ generated source for class X """
    def minDist(self, arr, n, x, y):
        """ generated source for method minDist """
        i = 0
        min_dist = Integer.MAX_VALUE
        prev = 0
        while i < n:
            if arr[i] == x or arr[i] == y:
                if arr[prev] != arr[i] and (i - prev) < min_dist:
                    min_dist = i - prev
                    prev = i
                else:
                    prev = i
            i += 1
        return min_dist

