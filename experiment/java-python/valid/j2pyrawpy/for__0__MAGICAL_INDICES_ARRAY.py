#!/usr/bin/env python
""" generated source for module for__0__MAGICAL_INDICES_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def solve(cls, A, n):
        """ generated source for method solve """
        i = int()
        cnt = 0
        j = int()
        parent = [None]*n + 1
        vis = [None]*n + 1
        while i < n:
            j = i
            if parent[j] == -1:
                while parent[j] == -1:
                    parent[j] = i
                    j = (j + A[j] + 1) % n
                if parent[j] == i:
                    while vis[j] == 0:
                        vis[j] = 1
                        cnt += 1
                        j = (j + A[j] + 1) % n
            i += 1
        return cnt

