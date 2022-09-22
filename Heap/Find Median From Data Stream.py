# (295. Hard) he median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.

# Solution 1 : Brute Force O(n) time and space
# Maintain a single ordered list, which has the elements in order.
# When we have to find the median, it becomes easy, as we can exract out the 2 middle elements.

# Solution 2 : O(logn) Using 2 heaps - maxHeap and minHeap
# Inserting or Removing element from a heap is O(logn).
# In maxHeap, finding the max is O(1) operation. Similarly, in minHeap finding the min is O(1).

# We will split the ordered list we want into 2 - small heap, large heap. Ex: [1,2,3,4]. Small heap - [1,2]. Large Heap - [3,4]
# We always have to balance the elements btw 2 heaps. The diff should not be greater than 1.
# Ex: Lenght of small heap = large heap = 2 is allowed. Lenght of small heap = 1, Lenght of small heap = 2 is allowed Or vice-versa.
# But, if Lenght of small heap =3, and Lenght of large heap = 1, that's not allowed. We will have to balance the heaps then.

# Small heap is implemented using maxHeap, and large heap using minHeap; coz we are interested in the middle elements.
# If length of 2 heaps in same, then we take the max from small heap and min from large heap; and take the avg of 2.
# If the length of 2 heaps is not same, then if small heap is more; we take the max from that heap as the median.
# If the large heap is more, then we take the min from that heap as the median.

# Algorithm : 
# By default insert elements into small heap first. Ex : [2,3,7]
# First add 2 to small heap. Then add 3 to small heap. Adding is O(logn).
# Now the lenght of 2 heaps is not same, so take the max from small heap and insert it into large heap. O(1) is lookup time and to insert it takes O(logn).
# Next add 7 to small heap.
# We also have to check another condition, which is all elements in small heap <= all elements in large heap.
# Since, this is not satisfied, again find the max from small heap and insert it into large heap.

# IMP : By default, python implements only minHeap. To implement maxHeap, we have to multiple the number by -1, before putting it into the heap.

from heapq import heappush,heappop
class MedianFinder:
    # O(logn) using 2 heaps
    def __init__(self):
        # Small heap - maxHeap. Large heap - minHeap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Since, theres no maxHeap in Python, multiply by -1
        heappush(self.small,-1 * num)
        # Check if all elements in small <= all elements in large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large,val)
        
        # Uneven size ?
        if len(self.small) > len(self.large)+1:
            val = -1 * heappop(self.small)
            heappush(self.large,val)
        
        if len(self.large) > len(self.small)+1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
