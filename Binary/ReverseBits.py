# (190. Easy) Reverse bits of a given 32 bits unsigned integer.

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2:

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

# Constraints:

# The input must be a binary string of length 32

# Solution 1 : O(32) time
# 1. Do the following 32 times (because we have 32 bit integer)
# 2. left shift res by 1 (Since we want to reverse the bits. The 0th bit should occupy 31st bit place. Hence over the course of 32 loops, it will end up occupying the correct place)
# 3. add n&1 to res (Basically, get the value of one bit at a time and add it to the res)
# 4. right shift n by 1 (To move to the next bit)

class Solution:
    # O(32) time
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1
            res = res + (n&1)
            n = n >> 1
        return res
        