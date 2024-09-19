"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

"""

def binary_search(nums, target):
    # Initialize two pointers for the start and end of the list
    left, right = 0, len(nums) - 1
    
    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        # If target is smaller than the middle element, search the left half
        elif nums[mid] > target:
            right = mid - 1
        # If target is larger than the middle element, search the right half
        else:
            left = mid + 1
            
    # If the target is not found, return -1
    return -1
