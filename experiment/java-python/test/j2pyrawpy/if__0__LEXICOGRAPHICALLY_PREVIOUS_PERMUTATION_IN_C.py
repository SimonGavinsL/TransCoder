#!/usr/bin/env python
""" generated source for module if__0__LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C """
class X(object):
    """ generated source for class X """
    @classmethod
    def prevPermutation(cls, str_):
        """ generated source for method prevPermutation """
        n = str_.length - 1
        i = n
        while i > 0 and str_[i - 1] <= str_[i]:
            i -= 1
        j = i - 1
        while j + 1 <= n and str_[j + 1] <= str_[i - 1]:
            j += 1
        swap(str_, i - 1, j)
        sb = StringBuilder(String.valueOf(str_))
        sb.reverse()
        str_ = sb.__str__().toCharArray()
        return True

