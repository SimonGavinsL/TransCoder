#!/usr/bin/env python
""" generated source for module for__0__FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumNodes(cls, l):
        """ generated source for method sumNodes """
        leafNodeCount = (Math.pow(2, l - 1))
        vec = Vector()
        i = 1
        while i <= leafNodeCount:
            i += 1
        i = l - 2
        while i >= 0:
            while k < vec.get(i + 1).size() - 1:
                vec.get(i).add(vec.get(i + 1).get(k) + vec.get(i + 1).get(k + 1))
                k += 2
            i -= 1
        sum = 0
        i = 0
        while i < l:
            while j < vec.get(i).size():
                j += 1
            i += 1
        return sum

