# (146. Medium) 
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


# Solution : We implement solution using doubly linked list. Most recently used value is put at the front of the list, and least used is put at the end. Hence the choice of doubly LL, since its easier to add nodes in the front and remove nodes in the end.
# Plus we will have two reference nodes in the start and in the end. Start node is denoted with {0:0} and end node is denoted with {-1:-1}
# Since we want get and put must each run in O(1) average time, we will use a dictionary to keep track of the already added keys. Their value would be the actual node. In that way we can access it in O(1) time.
# We store the capacity using self.capacity variable

class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insertIntoHead(self,node):
        headNext = self.head.next
        # 4 pointers need to be updated. We are inserting it after the first Node position
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
        self.head.next = node

    def deleteFromTail(self):
        if len(self.dict)==0: return
        # One before the tail node is the actual Node
        tailNode = self.tail.prev
        del self.dict[tailNode.key]
        self.deleteFromList(tailNode)

    def deleteFromList(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.deleteFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.deleteFromList(node)
            node.value = value
            self.insertIntoHead(node)
        else:
            if len(self.dict)>=self.capacity:
                self.deleteFromTail()
            newNode = ListNode(key,value)
            self.dict[key] = newNode
            self.insertIntoHead(newNode)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)