"""
*** Problem Identification ***
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

*** Solution ***
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter

    # Count the frequency of each letter in magazine
    magazine_count = Counter(magazine)
    
    # Traverse through each letter in ransomNote
    for letter in ransomNote:
        # Check if the letter is available in magazine with required frequency
        if magazine_count[letter] > 0:
            magazine_count[letter] -= 1
        else:
            return False
    
    return True

print (canConstruct("ball", "ballers"))
