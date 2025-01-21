from typing import Optional

class ListNode:
    def __init__(self, x, next_node =None):
        self.val = x
        self.next = next_node

    def __repr__(self):
        return f"{self.val}"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head

        if slow.next is not None:
            fast = slow.next
        else:
            return False

        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

minus_four = ListNode(-4)
zero = ListNode(0, minus_four)
two = ListNode(2, zero)
three = ListNode(3, two)
four = ListNode(4, three)
minus_four.next = four
four.next = zero

head = zero
#
# str = ""
# while head:
#     str += f"{head.val}->"
#     head = head.next

print(str)
print(Solution().hasCycle(head))
