# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Ex 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Solution 1 : Iterative Approach
# First you initialize dummy and temp. One is sitting at the start of the linkedlist and the other (temp) is going to move forward
#  find which value should be added to the list. Note that it's initialized with a value 0 but it can be anything! You initialize 
#  it with your value of choice! Doesn't matter since we're going to finally return dummy.next which disregards 0 that we used to 
#  start the linkedlist. Line #1 makes sure none of the l1 and l2 are empty! If one of them is empty, 
#  we should return the other! If both are nonempty, we check val of each of them to add the smaller one to the result linkedlist! 
#  In line #2, l1.val is smaller and we want to add it to the list. How? We use temp POINTER (it's pointer, remember that!). 
#  Since we initialized temp to have value 0 at first node, we use temp.next to point 0 to the next value we're going to add to 
#  the list l1.val (line #3). Once we do that, we update l1 to go to the next node of l1. If the if statement of line #2 doesn't work, we do similar stuff with l2. And finally, if the length of l1 and l2 are not the same, we're going to the end of one of them at some point! Line #5 adds whatever left from whatever linkedlist to the temp.next (check the above video for a great explanation of this part). Note that both linkedlists were sorted initially. Also, this line takes care of when one of the linkedlists are empty. Finally, we return dummy.next since dummy is pointing to 0 and next to zero is what we've added throughout the process.

# Time: O(m+n) which is the lenght of 2 ll's, Space : O(1)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        dummy = temp = ListNode(0)
        while l1 and l2: #1

            if l1.val < l2.val: #2
                temp.next = l1 #3
                l1 = l1.next #4
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next   # IMP : Move on to the next element
        temp.next = l1 or l2  #5
        return dummy.next #6

# Solution 2 : Recursive Approach
# Another way of solving is problem is by doing recursion. The first check is obvious! If one of them is empty, return the other one! Similar to line 
#5 of previous solution. Here, we have two cases, whatever list has the smaller first element (equal elements also satisfies line #1), will be returned at the end. 
# In the example l1 = [1,2,4], l2 = [1,3,4], we go in the if statement of line #1 first, this means that the first element of l1 doesn't get changed! Then, we move the pointer to the second element of l1 by calling the function again but with l1.next and l2 as input! This round of call, goes to line #2 because now we have element 1 from l2 versus 2 from l1. Now, basically, l2 gets connected to the tail of l1. 
# We keep moving forward by switching between l1 and l2 until the last element. 

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val: #1
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else: #2
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2 