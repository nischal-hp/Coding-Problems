# 141. Easy Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Solution 1 : O(n) space
# We can use a Dictionary to store the Node at every point. At any time, if we encounter node which is already in Dict, that 
# means there is a cycle in the LL.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) - Dictionary approach - Store the entire Node, not just the value
        dictionary = {}
        while head:
            if head in dictionary: 
                return True
            else: 
                dictionary[head]= True
            head = head.next
        return False

# Solution 2 : O(1) space, using 2 pointer approach - slow and fast pointers
# A slow pointer will point the next node, whereas fast pointer will point to the next to next node.
# At any point if slow==fast, then there is a cycle in LL.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two Pointer approach, using Slow and Fast pointers
        slow = fast = head
        while fast and fast.next:  # Since we access, fast.next.next; we first have to check if fast.next exists or not
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False