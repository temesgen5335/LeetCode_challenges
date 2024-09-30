"""
*** Problem Identification ***

Pascal's Triangle II
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

* Solution ***
"""

def getRow(rowIndex):
    # Initialize the first row of Pascal's triangle
    row = [1]  # The 0-th row
    
    # Build the triangle row by row
    for i in range(1, rowIndex + 1):
        # Create a new row based on the previous one
        new_row = [1]  # Start with the first element as 1
        
        # Calculate the intermediate values
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        
        new_row.append(1)  # End with the last element as 1
        row = new_row  # Move to the next row
    
    return row

# Example usage
print(getRow(3))  # Output: [1, 3, 3, 1]
print(getRow(0))  # Output: [1]
print(getRow(1))  # Output: [1, 1]
