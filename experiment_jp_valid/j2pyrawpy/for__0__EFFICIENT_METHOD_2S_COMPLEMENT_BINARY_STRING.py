#!/usr/bin/env python
""" generated source for module for__0__EFFICIENT_METHOD_2S_COMPLEMENT_BINARY_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def findTwoscomplement(cls, str_):
        """ generated source for method findTwoscomplement """
        n = len(str_)
        i = int()
        if i == -1:
            return "1" + str_
        k = i - 1
        while k >= 0:
            if str_.charAt(k) == '1':
                str_.replace(k, k + 1, "0")
            else:
                str_.replace(k, k + 1, "1")
            k -= 1
        return str_.__str__()

