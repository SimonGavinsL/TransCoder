#!/usr/bin/env python
""" generated source for module for__0__PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxDifference(cls, arr, N, k):
        """ generated source for method maxDifference """
        M = int()
        S = 0
        S1 = 0
        max_difference = 0
        temp = int()
        i = 0
        while i < N:
            while j < N:
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                j += 1
            i += 1
        M = Math.max(k, N - k)
        i = 0
        while i < M:
            i += 1
        max_difference = S1 - (S - S1)
        return max_difference

