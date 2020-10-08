#!/usr/bin/env python
""" generated source for module if__0__CHECK_IF_STACK_ELEMENTS_ARE_PAIRWISE_CONSECUTIVE """
class X(object):
    """ generated source for class X """
    @classmethod
    def pairWiseConsecutive(cls, s):
        """ generated source for method pairWiseConsecutive """
        aux = Stack()
        while not s.isEmpty():
            aux.push(s.peek())
            s.pop()
        result = True
        while len(aux) > 1:
            aux.pop()
            aux.pop()
            if Math.abs(x - y) != 1:
                result = False
            s.push(x)
            s.push(y)
        return result

