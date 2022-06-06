# (Medium) Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Solution 1 : Writing a helper function to determine the lenght of LL. Two Pass Solution
# Once we know the length of LL, we can determine what position has to be removed. 
# Using a cunter can keep track of it, and make suitable changes to LL.

# Time : O(n), Space : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthll(head)
        count=0
        origHead = head  # To be able to finally return it.
        if n==length==1:  # Supporting example 2
            return None
        if n==length:   # Supporting corner cases, where head=[1,2] and n=2
            return head.next
        while head and n<=length:
            if count==length-n-1:
                head.next=head.next.next
            head=head.next
            count+=1
        return origHead
    
    def lengthll(self,head):
        length=0
        while head:
            head=head.next
            length+=1
        return length

# Solution 2 : Single Pass Solution. Time and Space : same as before
# We are required to remove the nth node from the end of list. For this, we need to traverse N - n nodes from the start of the list, where N is the length of linked list. We can do this in one-pass as follows -
# Let's assign two pointers - fast and slow to head. We will first iterate for n nodes from start using the fast pointer.
# Now, between the fast and slow pointers, there is a gap of n nodes. Now, just Iterate and increment both the pointers till fast reaches the last node. The gap between fast and slow is still of n nodes, meaning that slow is nth node from the last node (which currently is fast).

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=head
        count=0
        while count!=n:  # This is to keep the fast pointer at a distance of n from slow pointer
            fast=fast.next
            count+=1
        if fast==None:  # In the case where lenght of LL=n. Then just return excluding the head
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next  # Step where node is deleted.
        return head