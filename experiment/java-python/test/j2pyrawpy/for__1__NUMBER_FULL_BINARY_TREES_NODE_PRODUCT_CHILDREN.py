#!/usr/bin/env python
""" generated source for module for__1__NUMBER_FULL_BINARY_TREES_NODE_PRODUCT_CHILDREN """
class X(object):
    """ generated source for class X """
    @classmethod
    def numoffbt(cls, arr, n):
        """ generated source for method numoffbt """
        maxvalue = -2147483647
        minvalue = 2147483647
        mark = [None]*maxvalue + 2
        value = [None]*maxvalue + 2
        Arrays.fill(mark, 0)
        Arrays.fill(value, 0)
        ans = 0
        i = minvalue
        while i <= maxvalue:
            if mark[i] != 0:
                while j <= maxvalue and j / i <= i:
                    if mark[j] == 0:
                        continue 
                    value[j] = value[j] + (value[i] * value[j / i])
                    if i != j / i:
                        value[j] = value[j] + (value[i] * value[j / i])
                    j += i
            ans += value[i]
            i += 1
        return ans

