#!/usr/bin/env python
""" generated source for module for__0__PRINT_DIGITS_POSITION_REMOVED_MAKE_NUMBER_DIVISIBLE_6 """
class X(object):
    """ generated source for class X """
    @classmethod
    def greatest(cls, s):
        """ generated source for method greatest """
        n = len(s)
        a = [None]*n
        sum = 0
        if a[n - 1] % 2 != 0:
            if a[n - 2] % 2 != 0 or (sum - a[n - 1]) % 3 != 0:
                print " - 1"
            else:
                print n
        else:
            while i < n - 1:
                if (a[i]) % 3 == re:
                    if a[i + 1] > a[i]:
                        del_ = i
                        flag = 1
                        break
                    else:
                        del_ = i
                i += 1
            if flag == 0:
                if a[n - 2] % 2 == 0 and re == a[n - 1] % 3:
                    del_ = n - 1
            if del_ == -1:
                print -1
            else:
                print del_ + 1

