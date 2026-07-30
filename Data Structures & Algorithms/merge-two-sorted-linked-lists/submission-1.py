# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Intuition: like merge question, compare the two values of each list. Then once emptied, add the rest of the non-emptied list to the end.
# O(n+m) time, n being list1, m being list2
# O(min(n, m)) space complexity, since I just add the rest of the list node to the end once the first while loop ends. 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        while list1 and list2:
            # Check
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next       
            else: 
                temp.next = list2
                temp = temp.next
                list2 = list2.next

        if list1 == None:
            temp.next = list2
        else:
            temp.next = list1


        return head.next
