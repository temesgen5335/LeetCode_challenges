"""*** Problem Identification***

Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

*** solution ***
"""
def combinationSum2(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        
        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] == prev:  # skip duplicates
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])
            prev = candidates[i]
    
    candidates.sort()  # Sort to handle duplicates
    result = []
    backtrack(0, [], target)
    return result