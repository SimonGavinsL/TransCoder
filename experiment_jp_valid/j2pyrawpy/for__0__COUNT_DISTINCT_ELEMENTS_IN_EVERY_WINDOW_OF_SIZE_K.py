#!/usr/bin/env python
""" generated source for module for__0__COUNT_DISTINCT_ELEMENTS_IN_EVERY_WINDOW_OF_SIZE_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDistinct(cls, arr, k):
        """ generated source for method countDistinct """
        hM = HashMap()
        dist_count = 0
        print dist_count
        i = k
        while i < arr.length:
            if hM.get(arr[i - k]) == 1:
                hM.remove(arr[i - k])
                dist_count -= 1
            else:
                hM.put(arr[i - k], count - 1)
            if hM.get(arr[i]) == None:
                hM.put(arr[i], 1)
                dist_count += 1
            else:
                hM.put(arr[i], count + 1)
            print dist_count
            i += 1

