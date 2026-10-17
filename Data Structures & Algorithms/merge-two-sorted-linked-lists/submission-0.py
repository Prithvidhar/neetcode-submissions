# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        other = None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = list1
            other = list2
        else:
            head = list2
            other = list1
        curr = head
        while(curr.next != None):
            temp = curr.next
            if curr.next.val > other.val:
                curr.next = other
                other = temp
            curr = curr.next
        curr.next = other
        return head
        