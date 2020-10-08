#!/usr/bin/env python
""" generated source for module if__0__CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES """
class X(object):
    """ generated source for class X """
    @classmethod
    def isRotated(cls, str1, str2):
        """ generated source for method isRotated """
        clock_rot = " "
        anticlock_rot = " "
        len = len(str2)
        anticlock_rot = anticlock_rot + str2.substring(len - 2, len) + str2.substring(0, len - 2)
        clock_rot = clock_rot + str2.substring(2) + str2.substring(0, 2)
        return (str1 == clock_rot or str1 == anticlock_rot)

