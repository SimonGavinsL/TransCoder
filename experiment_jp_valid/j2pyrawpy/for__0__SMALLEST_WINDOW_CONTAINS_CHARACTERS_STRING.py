#!/usr/bin/env python
""" generated source for module for__0__SMALLEST_WINDOW_CONTAINS_CHARACTERS_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def findSubString(cls, str_):
        """ generated source for method findSubString """
        n = len(str_)
        dist_count = 0
        visited = [None]*MAX_CHARS
        Arrays.fill(visited, False)
        start = 0
        start_index = -1
        min_len = Integer.MAX_VALUE
        count = 0
        curr_count = [None]*MAX_CHARS
        j = 0
        while j < n:
            curr_count[str_.charAt(j)] += 1
            if curr_count[str_.charAt(j)] == 1:
                count += 1
            if count == dist_count:
                while curr_count[str_.charAt(start)] > 1:
                    if curr_count[str_.charAt(start)] > 1:
                        curr_count[str_.charAt(start)] -= 1
                    start += 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start
            j += 1
        return str_.substring(start_index, start_index + min_len)

