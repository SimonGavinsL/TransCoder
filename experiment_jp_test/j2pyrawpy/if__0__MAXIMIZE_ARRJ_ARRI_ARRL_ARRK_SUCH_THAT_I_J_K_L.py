#!/usr/bin/env python
""" generated source for module if__0__MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxValue(cls, arr, n):
        """ generated source for method findMaxValue """
        table1 = [None]*n + 1
        table2 = [None]*n
        table3 = [None]*n - 1
        table4 = [None]*n - 2
        Arrays.fill(table1, Integer.MIN_VALUE)
        Arrays.fill(table2, Integer.MIN_VALUE)
        Arrays.fill(table3, Integer.MIN_VALUE)
        Arrays.fill(table4, Integer.MIN_VALUE)
        return table4[0]

