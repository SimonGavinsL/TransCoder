#!/usr/bin/env python
""" generated source for module if__0__COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWords(cls, str_, len):
        """ generated source for method countWords """
        count = 1
        if str_.charAt(0) == str_.charAt(1):
            count *= 1
        else:
            count *= 2
        if str_.charAt(len - 1) == str_.charAt(len - 2):
            count *= 1
        else:
            count *= 2
        return count

