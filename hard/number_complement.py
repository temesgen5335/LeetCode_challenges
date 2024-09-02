"""
*** Problem Identification ***

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 
*** Solution ***
"""

def findComplement(num):
    # Step 1: Find the number of bits in num
    num_bits = num.bit_length()
    
    # Step 2: Create a mask with all bits set to 1 of length num_bits
    mask = (1 << num_bits) - 1
    
    # Step 3: Compute the complement
    complement = num ^ mask
    
    return complement

#exacmple usecase
print(findComplement(1))