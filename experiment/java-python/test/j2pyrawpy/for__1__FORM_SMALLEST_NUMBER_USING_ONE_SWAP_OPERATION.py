#!/usr/bin/env python
""" generated source for module for__1__FORM_SMALLEST_NUMBER_USING_ONE_SWAP_OPERATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def smallestNumber(cls, str_):
        """ generated source for method smallestNumber """
        num = str_.toCharArray()
        n = len(str_)
        rightMin = [None]*n
        rightMin[n - 1] = -1
        right = n - 1
        small = -1
        if small != -1:
            temp = num[0]
            num[0] = num[small]
            num[small] = temp
        else:
            while i < n:
                if rightMin[i] != -1:
                    temp = num[i]
                    num[i] = num[rightMin[i]]
                    num[rightMin[i]] = temp
                    break
                i += 1
        return (str(num))

