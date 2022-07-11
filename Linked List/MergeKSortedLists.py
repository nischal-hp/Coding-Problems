# (23. Hard) You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.

# Solution 1 : Brute Force. O(nlogn) time, and O(n) space, where n is the total number of nodes in the lists
# Traverse all the linked lists and collect the values of the nodes into an array.
# Sort and iterate over this array to get the proper value of nodes.
# Create a new sorted linked list and extend it with the new nodes.

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

# Solution 2 : Compare one by one. O(kn) time and O(1) space, where k-total number of linked lists
# Compare every k nodes (head of every linked list) and get the node with the smallest value.
# Extend the final sorted linked list with the selected nodes.

# Solution 3 : Optimize above by using Priority Queue. - Avoid this approach, might error out
# O(nlogk) time and space is O(n) or O(k) due to priority queue
# Time : 
# The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
# Space : 
# O(n) Creating a new linked list costs O(n) space.
# The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).
from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


# Solution 4 : Merge two lists at a time, which will be similar to mergeTwoSortedLists problem.
# O(kn) time and O(1) space

class Solution:
    # O(kn) time, O(1) space solution
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        result = self.mergeTwoSortedLists(lists[0],lists[1])
        for i in range(2,len(lists)):
            result=self.mergeTwoSortedLists(result,lists[i])
        return result
    def mergeTwoSortedLists(self,l1,l2):
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

# Solution 5 : Above can be optimized by using Divide and Conquer approach
# O(nlogk) time and O(1) space. 
# We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
# Sum up the merge process and we can get O(nlogk)

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])   # Can pass in indices to make it truly O(1) space
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next