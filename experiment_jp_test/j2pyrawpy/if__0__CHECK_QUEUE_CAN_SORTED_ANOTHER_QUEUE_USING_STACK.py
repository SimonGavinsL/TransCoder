#!/usr/bin/env python
""" generated source for module if__0__CHECK_QUEUE_CAN_SORTED_ANOTHER_QUEUE_USING_STACK """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkSorted(cls, n):
        """ generated source for method checkSorted """
        st = Stack()
        expected = 1
        fnt = int()
        while len(q) != 0:
            fnt = q.peek()
            q.poll()
            if fnt == expected:
                expected += 1
            else:
                if len(st) == 0:
                    st.push(fnt)
                elif len(st) != 0 and st.peek() < fnt:
                    return False
                else:
                    st.push(fnt)
            while len(st) != 0 and st.peek() == expected:
                st.pop()
                expected += 1
        return False

