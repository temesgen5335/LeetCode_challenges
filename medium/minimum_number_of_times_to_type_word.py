
"""
** Problem Identification**

You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.


Constraints:

1 <= word.length <= 105
word consists of lowercase English letters.


"""
from collections import Counter

def min_pushes_to_type_word(word):
    # Step 1: Count the frequency of each character in the word
    char_count = Counter(word)
    
    # Step 2: Get the frequencies sorted in descending order
    frequencies = sorted(char_count.values(), reverse=True)

    # Step 3: Calculate the minimum pushes required
    total_pushes = 0
    presses_per_key = 1  # Start with 1 push for the first key

    for i, freq in enumerate(frequencies):
        # Determine how many presses are needed based on the index
        total_pushes += freq * presses_per_key
        
        # Every 3 letters will increase the presses needed
        if (i + 1) % 3 == 0:
            presses_per_key += 1

    return total_pushes

# Example usage
print(min_pushes_to_type_word("abcde"))             # Output: 5
print(min_pushes_to_type_word("xyzxyzxyzxyz"))      # Output: 12
print(min_pushes_to_type_word("aabbccddeeffgghhiiiiii"))  # Output: 24