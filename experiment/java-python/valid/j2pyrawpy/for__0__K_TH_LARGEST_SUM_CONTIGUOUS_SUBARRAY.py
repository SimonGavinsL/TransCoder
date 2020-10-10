#!/usr/bin/env python
""" generated source for module for__0__K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def kthLargestSum(cls, arr, n, k):
        """ generated source for method kthLargestSum """
        sum = [None]*n + 1
        sum[0] = 0
        sum[1] = arr[0]
        Q = PriorityQueue()
        i = 1
        while i <= n:
            while j <= n:
                if len(Q) < k:
                    Q.add(x)
                else:
                    if Q.peek() < x:
                        Q.poll()
                        Q.add(x)
                j += 1
            i += 1
        return Q.poll()

