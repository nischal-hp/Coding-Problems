# (371. Medium) Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000

# Solution 1 : O(n) time. Using xor and or operation in a loop
# We have to go for binary represenation of numbers.
# If its 1+0 or 0+1 = 1. If its 1+1 or 0+0 = 0. The operation which gives us this logic is XOR.
# Coming to the carry bit. This is generated only when both are 1's. That is only for 1+1.
# Hence, we can use AND operation, as it generates 1 only when both are 1's. However we need to left shift it by 1, to make sure that its applied to the next bit.
# Finally, we again XOR the above 2 results, until the carry bit is = 0, at which stage we are done with the operation.

# Mask is required to hanled the case of negative numbers:
# Lets have a look, say we are adding -2 and 3, which = 1

# In Python this would be ( showing only 3 bits for clarity )

# 1 1 0 +
# 0 1 1

# Using binary addition we would get:
# 0 0 1

# That seems fine but what happended to the extra carry bit ? ( 1 0 0 0 ), if we were doing this by hand we would simply ignore it, but Python does not, instead it continues 'adding' that bit and continuing the sum.

# 1 1 1 1 1 1 0 +
# 0 0 0 0 0 1 1
# 0 0 0 1 0 0 0 + ( carry bit )

# so this actually continues on forever unless, we make use of a mask

# The logic behind a mask is really simple, you should know that x & 1 = x right, so using that simple principle,
# if we create a series of 4 1's and & them to any larger size series, we will get just that part of the series we want, so

# 1 1 1 1 1 0 0 1
# 0 0 0 0 1 1 1 1 &

# 0 0 0 0 1 0 0 1 ( Important to note that using a mask removes the two's compliment)

# For this question leetcode uses 32 bits, so you just need to create a 32 bit mask of 1's , the quickest way is to use hexadecimal and 0xffffffff, you can write the binary form if you prefer it will work the same.

# Note the final check, if b = 0 that means the carry bit 'finished', but when there is a negative number ( like -1), the carry bit will continue until it exceeds our 32 bit mask ( to end while loop ) it wont be 0 so in that case we use the mask.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
        