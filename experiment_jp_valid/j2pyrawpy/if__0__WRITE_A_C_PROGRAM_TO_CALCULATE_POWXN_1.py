#!/usr/bin/env python
""" generated source for module if__0__WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def power(cls, x, y):
        """ generated source for method power """
        temp = float()
        temp = power(x, y / 2)
        if y % 2 == 0:
            return temp * temp
        else:
            if y > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x

