"""
*** Problem Identification ***
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

*** solution ***
"""

from collections import Counter
import heapq

def topKFrequent(nums, k):
    # Step 1: Count frequencies of each element
    count = Counter(nums)
    
    # Step 2: Use a min-heap to keep track of the top k frequent elements
    # The heap will store tuples of (frequency, element)
    heap = []
    
    for num, freq in count.items():
        # We push tuples (frequency, element) into the heap
        heapq.heappush(heap, (freq, num))
        
        # If the heap exceeds size k, remove the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Step 3: Extract the elements from the heap
    top_k_elements = [num for freq, num in heap]
    
    return top_k_elements

grades = [80,90, 60,100,100,90,70,70,60,70,60]
print (topKFrequent(grades, 2))