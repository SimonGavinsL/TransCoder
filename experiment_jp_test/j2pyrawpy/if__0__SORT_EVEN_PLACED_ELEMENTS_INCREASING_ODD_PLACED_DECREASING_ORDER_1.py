#!/usr/bin/env python
""" generated source for module if__0__SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def bitonicGenerator(cls, arr, n):
        """ generated source for method bitonicGenerator """
        i = 1
        j = n - 1
        while i < j:
            arr = swap(arr, i, j)
            i += 2
            j -= 2
        Arrays.sort(arr, 0, (n + 1) / 2)
        Arrays.sort(arr, (n + 1) / 2, n)
        low = (n + 1) / 2
        high = n - 1
        while low < high:
            arr[low] = arr[high]
            arr[high] = temp
            low += 1
            high -= 1

