# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]):
        return self.reverse_list_recursion(head)
        # return self.reverse_list_iterative(head)

    def reverse_list_recursion(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head

        reversed_head = self.reverse_list_recursion(head.next)
        head.next.next = head
        head.next = None

        return reversed_head

    def reverse_list_iterative(self, head:Optional[ListNode]):
        prev = None
        fwd_pointer = head.next

        while fwd_pointer:
            head.next = prev
            prev = head
            head = fwd_pointer
            fwd_pointer = head.next

        head.next = prev
        return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

head = one
str = ""

while head:
    str += f"{head.val}->"
    head = head.next
print(str)

head = one
newhead = Solution().reverseList(head)
print("reversed")

str = ""
while newhead:
    str += f"{newhead.val}->"
    newhead = newhead.next
print(str)


