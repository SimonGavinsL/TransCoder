#!/usr/bin/env python
""" generated source for module for__1__FIND_K_SUCH_THAT_ALL_ELEMENTS_IN_KTH_ROW_ARE_0_AND_KTH_COLUMN_ARE_1_IN_A_BOOLEAN_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def find(cls, arr):
        """ generated source for method find """
        i = 0
        j = n - 1
        res = -1
        while i < n and j >= 0:
            if arr[i][j] == False:
                while j >= 0 and (arr[i][j] == False or i == j):
                    j -= 1
                if j == -1:
                    res = i
                    break
                else:
                    i += 1
            else:
                while i < n and (arr[i][j] == True or i == j):
                    i += 1
                if i == n:
                    res = j
                    break
                else:
                    j -= 1
        if res == -1:
            return res
        return res

