# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Ex 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Ex 2:
# Input: head = []
# Output: []

# Solution : Both Iterative and Recursive solution exist for this.

# Solution 1 : Iterative :

class Solution:
    def reversell(self,head):
        prev= None  # Two Variables to store prev and current Node in LL
        curr=head
        while curr:
            next=curr.next   # Save the next value in a temp variable
            curr.next=prev   # Point next to the prev node
            prev=curr        # Iterate to the next node
            curr=next        # Iterate curr to the next node
        return prev          # Prev would be the new head. curr would be None by the end of the loop

# Solution 2 : Recursive :
# Here would need another parameter inside function which points to the prev Node

class Solution:
    def reversell(self,head,prev=None):
        if not head:     # Base Case of Last Node. Return Prev, which would be the actual node. head would point to None
            return prev
        temp = head.next    # Set head.next to prev Node and store head.next in a temp variable
        head.next=prev      
        return self.reversell(temp,head)   # Recursively call the function with temp which will be the new head; and curr head would be prev
