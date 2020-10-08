#!/usr/bin/env python
""" generated source for module if__0__CHECK_IF_ARRAY_ELEMENTS_ARE_CONSECUTIVE """
class X(object):
    """ generated source for class X """
    def areConsecutive(self, arr, n):
        """ generated source for method areConsecutive """
        min = getMin(arr, n)
        max = getMax(arr, n)
        if max - min + 1 == n:
            while i < n:
                if visited[arr[i] - min] != False:
                    return False
                visited[arr[i] - min] = True
                i += 1
            return True
        return False

