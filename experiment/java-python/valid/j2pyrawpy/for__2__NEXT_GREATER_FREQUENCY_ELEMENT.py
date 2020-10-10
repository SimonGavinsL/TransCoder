#!/usr/bin/env python
""" generated source for module for__2__NEXT_GREATER_FREQUENCY_ELEMENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def NFG(cls, a, n, freq):
        """ generated source for method NFG """
        s = Stack()
        s.push(0)
        res = [None]*n
        while len(s) > 0:
            res[s.peek()] = -1
            s.pop()

