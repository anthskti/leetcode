# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we return the list with the nth number removed
        # the difficult structure to to find the end of the list. 
        # my intuitive way is to calc the the length, subtract the length from the end and remove that node, inverse

        # dummy = ListNode(0, head) # sits before the linked list
        # temp = head
        
        # # counts the list
        # count = 0
        # while temp:
        #     count += 1
        #     temp = temp.next
        
        # count -= n
        # temp = dummy

        # # prev to the one that needs to be removed, w dummy, it should withdraw the -1
        # for i in range(count):
        #     temp = temp.next

        # if temp and temp.next:
        #     temp.next = temp.next.next
        # else:
        #     temp.next = None
        
        # return dummy.next
        
    # Time O(n), two passes through linked list
    # Space O(1)

        dummy = ListNode(0, head) # sits before the linked list
        slow, fast = dummy, dummy
        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
    
        return dummy.next

    # Two Pointer approach, fixed window
    # Time O(n) 
    # Space O(1)