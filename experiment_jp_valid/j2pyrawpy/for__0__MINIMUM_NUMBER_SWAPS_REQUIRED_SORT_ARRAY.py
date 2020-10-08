#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_NUMBER_SWAPS_REQUIRED_SORT_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minSwaps(cls, arr):
        """ generated source for method minSwaps """
        n = arr.length
        arrpos = ArrayList()
        arrpos.sort(Comparator())
        vis = [None]*n
        Arrays.fill(vis, False)
        ans = 0
        i = 0
        while i < n:
            if vis[i] or arrpos.get(i).getValue() == i:
                continue 
            while not vis[j]:
                vis[j] = True
                j = arrpos.get(j).getValue()
                cycle_size += 1
            if cycle_size > 0:
                ans += (cycle_size - 1)
            i += 1
        return ans

