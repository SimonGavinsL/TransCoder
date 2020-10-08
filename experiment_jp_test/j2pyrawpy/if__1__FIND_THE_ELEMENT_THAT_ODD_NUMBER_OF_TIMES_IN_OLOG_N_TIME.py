#!/usr/bin/env python
""" generated source for module if__1__FIND_THE_ELEMENT_THAT_ODD_NUMBER_OF_TIMES_IN_OLOG_N_TIME """
class X(object):
    """ generated source for class X """
    @classmethod
    def search(cls, arr, low, high):
        """ generated source for method search """
        mid = (low + high) / 2
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                cls.search(arr, mid + 2, high)
            else:
                cls.search(arr, low, mid)
        else:
            if arr[mid] == arr[mid - 1]:
                cls.search(arr, mid + 1, high)
            else:
                cls.search(arr, low, mid - 1)

