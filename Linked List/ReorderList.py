# (143. Medium) You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Ex 1 :
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Ex 2 :
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 
# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Solution 1 : O(n) time and O(n) space
# Intuitively can see that this can be implemented using a 2-pointer solution.
# But to be able to iterate backwards through the LL, we can first transfer over the values to an array
# Then iterate through the LL, and go on updating the values accordingly by referncing the array in the required order.
# If the length of LL is odd, make sure to also update the last element with the middle element.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(n) Time and Space
        """
        Do not return anything, modify head in-place instead.
        """
        llist=[]
        dummy=head
        while head!=None:
            llist.append(head.val)
            head=head.next
        i,j=0,len(llist)-1
        while i!=j and dummy.next:
            dummy.val=llist[i]
            dummy.next.val=llist[j]
            i+=1
            j-=1
            if dummy.next.next:        # Check to see if the element exists first
                dummy=dummy.next.next
            else:
                break
        if dummy and len(llist)%2!=0:  # If length of LL is odd
            dummy.val=llist[i]

# Solution 2 : O(n) time and O(1) space
# Can break the LL into two. We need to iterate in reverse order the second half of LL, but we have the links in the opposite way.
# So the easiest soln, is to reverse the second half of LL and then merge it with first half.
# Also, to break, we need to have a pointer at the middle element. One way is to find the length of LL, and then get the middle element from it.
# Or have 2 pointers - slow and fast. Initially, slow=head, fast=head.next. Iterating slow=slow.next,fast=fast.next.next
# Whenever fast.next==None or fast.next.next is out of the LL, then we can stop. Here the middle element would be slow.next, irrespective of odd or even element LL.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(n) Time and O(1) Space
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle element
        slow, fast = head, head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        # Reverse second half
        second = slow.next  # This is the middle element
        prev = slow.next = None # Set next pointer of middle element to None
        while second:
            tmp = second.next
            second.next=prev
            prev=second
            second=tmp
            
        # Merge Two Halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next =tmp1
            first=tmp1
            second=tmp2
            