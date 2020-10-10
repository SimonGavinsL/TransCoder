#!/usr/bin/env python
""" generated source for module if__0__GENERATING_DISTINCT_SUBSEQUENCES_OF_A_GIVEN_STRING_IN_LEXICOGRAPHIC_ORDER """
class X(object):
    """ generated source for class X """
    @classmethod
    def generate(cls, st, s):
        """ generated source for method generate """
        if not st.contains(s):
            st.add(s)
            while i < len(s):
                t = t.substring(0, i) + t.substring(i + 1)
                cls.generate(st, t)
                i += 1
        return

