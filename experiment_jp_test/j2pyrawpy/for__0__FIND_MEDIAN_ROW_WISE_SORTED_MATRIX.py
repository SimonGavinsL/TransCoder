#!/usr/bin/env python
""" generated source for module for__0__FIND_MEDIAN_ROW_WISE_SORTED_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def binaryMedian(cls, m, r, c):
        """ generated source for method binaryMedian """
        max = Integer.MIN_VALUE
        min = Integer.MAX_VALUE
        desired = (r * c + 1) / 2
        while min < max:
            while i < r:
                get = Arrays.binarySearch(m[i], mid)
                if get < 0:
                    get = Math.abs(get) - 1
                else:
                    while get < m[i].length and m[i][get] == mid:
                place = place + get
                i += 1
            if place < desired:
                min = mid + 1
            else:
                max = mid
        return min

