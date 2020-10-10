#!/usr/bin/env python
""" generated source for module for__0__SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER """
class X(object):
    """ generated source for class X """
    @classmethod
    def bitonicGenerator(cls, arr, n):
        """ generated source for method bitonicGenerator """
        evenArr = Vector()
        oddArr = Vector()
        Collections.sort(evenArr)
        Collections.sort(oddArr, Collections.reverseOrder())
        i = 0
        j = 0
        while j < len(evenArr):
        __i_0 = i
        i += 1
            arr[__i_0] = evenArr.get(j)
            j += 1
        j = 0
        while j < len(oddArr):
        __i_1 = i
        i += 1
            arr[__i_1] = oddArr.get(j)
            j += 1

