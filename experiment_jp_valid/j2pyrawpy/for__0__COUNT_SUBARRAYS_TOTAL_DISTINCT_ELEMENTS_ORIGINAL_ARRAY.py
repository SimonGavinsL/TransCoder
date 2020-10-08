#!/usr/bin/env python
""" generated source for module for__0__COUNT_SUBARRAYS_TOTAL_DISTINCT_ELEMENTS_ORIGINAL_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDistictSubarray(cls, arr, n):
        """ generated source for method countDistictSubarray """
        vis = HashMap()
        k = len(vis)
        vis.clear()
        ans = 0
        right = 0
        window = 0
        left = 0
        while left < n:
            while right < n and window < k:
                vis.put(arr[right], vis.get(arr[right]) + 1)
                if vis.get(arr[right]) == 1:
                    window += 1
                right += 1
            if window == k:
                ans += (n - right + 1)
            vis.put(arr[left], vis.get(arr[left]) - 1)
            if vis.get(arr[left]) == 0:
                window -= 1
            left += 1
        return ans

