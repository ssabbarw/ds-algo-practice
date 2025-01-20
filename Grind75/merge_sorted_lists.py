# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list2:
            return list1

        if not list1:
            return list2

        dummy_node = ListNode()
        merged_list_pointer = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                merged_list_pointer.next = list1
                merged_list_pointer = list1
                list1 = list1.next

            else:
                merged_list_pointer.next = list2
                merged_list_pointer = list2
                list2 = list2.next

        if not list1:
            merged_list_pointer.next = list2
        else:
            merged_list_pointer.next = list1

        return dummy_node.next