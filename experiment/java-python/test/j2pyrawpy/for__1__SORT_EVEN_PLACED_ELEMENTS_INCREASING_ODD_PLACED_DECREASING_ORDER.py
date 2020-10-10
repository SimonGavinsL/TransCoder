#!/usr/bin/env python
""" generated source for module for__1__SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER """
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
        while j < len(oddArr):
        __i_0 = i
        i += 1
            arr[__i_0] = oddArr.get(j)
            j += 1

