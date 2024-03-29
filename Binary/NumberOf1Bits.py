# (191. Easy) Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

# Constraints:

# The input must be a binary string of length 32.

# Solution 1 : O(32) or O(1) time. O(1) space
# Each time, we concentrating just on the last bit. We should count it, only if its 1.
# Hence we go for & operation. Ex: 101 & 1 = 001. Thus if we get a 1, we should increment our result.
# Since we have counted that bit, we dont need it anymore. Hence, we can right shift all bits by 1.
# We have to keep doing this, until all bits are not 0.

# Since input can be 32 bits long. The max it can run in O(32) or constant time, which means O(1).

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count

# Solution 2 : Same as above
# The above approach wastes time, in the sense; even if the bit is 0, we still have to repeat all the process.
# Instead what if we could just run the loop, based on the number of 1s in the input.
# The approach is to do : n= n & (n-1)
# Here at each stpe, we are eliminitaing one 1-bit at a time. Hence we can increment the result irrespective.
# Keep repeating the loop, until all bits are 0 in input.
# Try it with an example to understand it.

class Solution:
    # SOlution 2 : Alternate Solution
    def hammingWeight(self, n: int) -> int:
        count =0
        while n:
            n = n & (n-1)
            count+=1
        return count
        