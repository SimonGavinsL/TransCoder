#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxTasks(cls, high, low, n):
        """ generated source for method maxTasks """
        return Math.max(high[n - 1] + cls.maxTasks(high, low, (n - 2)), low[n - 1] + cls.maxTasks(high, low, (n - 1)))

