# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Intuition
# Singly, so I can't go back. 
# My guess, use two pointers. Since they want O(n) time, it'd be the best sol
# issue, you cannot go backwards on a linkedlist

# Solution has three steps
# 1. using the slow fast method to get to the middle.
# 2. Then reverse the middle -> end of the list. Makes it easier to reorder.
# 3. Using the pointer from 2, can have one pointer at the beginning and one at the middle, then take one from first half, and one from the second half. 
# Big note, you need to understand the core principal of "Reverse Linked List"  

# O(n) Time Complexity, O(1) Space Complexity (since its reorder) 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        # slow will land on the middle
        # fast will be at the end

        second = slow.next
        prev = None
        slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2
