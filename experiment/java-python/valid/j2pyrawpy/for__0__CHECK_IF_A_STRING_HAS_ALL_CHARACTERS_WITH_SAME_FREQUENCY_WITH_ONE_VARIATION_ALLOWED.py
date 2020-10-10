#!/usr/bin/env python
""" generated source for module for__0__CHECK_IF_A_STRING_HAS_ALL_CHARACTERS_WITH_SAME_FREQUENCY_WITH_ONE_VARIATION_ALLOWED """
class X(object):
    """ generated source for class X """
    @classmethod
    def isValidString(cls, str_):
        """ generated source for method isValidString """
        freq = [None]*CHARS
        i = int()
        freq1 = 0
        count_freq1 = 0
        while i < CHARS:
            if freq[i] != 0:
                freq1 = freq[i]
                count_freq1 = 1
                break
            i += 1
        j = int()
        freq2 = 0
        count_freq2 = 0
        while j < CHARS:
            if freq[j] != 0:
                if freq[j] == freq1:
                    count_freq1 += 1
                else:
                    count_freq2 = 1
                    freq2 = freq[j]
                    break
            j += 1
        k = j + 1
        while k < CHARS:
            if freq[k] != 0:
                if freq[k] == freq1:
                    count_freq1 += 1
                if freq[k] == freq2:
                    count_freq2 += 1
                else:
                    return False
            if count_freq1 > 1 and count_freq2 > 1:
                return False
            k += 1
        return True

