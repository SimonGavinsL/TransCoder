#!/usr/bin/env python
""" generated source for module for__0__FIND_THE_LARGEST_RECTANGLE_OF_1S_WITH_SWAPPING_OF_COLUMNS_ALLOWED """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxArea(cls, mat):
        """ generated source for method maxArea """
        hist = [None]*R + 1
        i = 0
        while i < R:
            while j < C:
                count[hist[i][j]] += 1
                j += 1
            while j >= 0:
                if count[j] > 0:
                    while k < count[j]:
                        hist[i][col_no] = j
                        col_no += 1
                        k += 1
                j -= 1
            i += 1
        curr_area = int()
        max_area = 0
        i = 0
        while i < R:
            while j < C:
                curr_area = (j + 1) * hist[i][j]
                if curr_area > max_area:
                    max_area = curr_area
                j += 1
            i += 1
        return max_area

