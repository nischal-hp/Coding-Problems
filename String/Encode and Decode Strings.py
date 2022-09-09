# (659. Medium) Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode.

# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

# Solution : Using length of string+ '#'+ actual string combination.
# While encoding, we first append the length of the string which is an integer converted to a string, followed by '#' sign,
# followed by the actual string itself.

# If we use just the # sign, then we wouldnt know if its added by us, or if its present in the actual string.
# So, it would be better to store the actual length of the string as well.

# While decoding, we keep looking for the # sign, and when we find it, we have found our marker.
# So based on the length, we can get the actual string, which comes after the # sign; append it to the result array.

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res