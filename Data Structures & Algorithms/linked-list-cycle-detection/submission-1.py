# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # our goal is to output a true or false value to prove if there is a cycle
        # this question has a intuitive solution
        # we have two pointers, have one move through the linked list normally, and have the other skip a node. 
        # if one of them can hit hit null, then its not cyclical.
        # if they both end up equallying to each other, then we can say there is a loop
        slow = head 
        fast = head

        while fast and fast.next:
            # skips initial case
            slow = slow.next
            fast = fast.next.next

            # check if the pointers are the same
            if slow == fast:
                return True 

        return False

# Time O(n) 
# Space O(1)
        