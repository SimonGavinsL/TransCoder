#!/usr/bin/env python
""" generated source for module for__0__CONSTRUCT_THE_ROOTED_TREE_BY_USING_START_AND_FINISH_TIME_OF_ITS_DFS_TRAVERSAL """
class X(object):
    """ generated source for class X """
    @classmethod
    def Restore_Tree(cls, S, End):
        """ generated source for method Restore_Tree """
        Identity = [None]*N
        parent = [None]*N
        Arrays.fill(parent, -1)
        curr_parent = Identity[0]
        j = 1
        while j < N:
            if End[child] - j > 1:
                parent[child] = curr_parent
                curr_parent = child
            else:
                parent[child] = curr_parent
                while parent[child] > -1 and End[child] == End[parent[child]]:
                    child = parent[child]
                    curr_parent = parent[child]
                    if curr_parent == Identity[0]:
                        break
            j += 1
        i = 0
        while i < N:
            i += 1
        return parent

