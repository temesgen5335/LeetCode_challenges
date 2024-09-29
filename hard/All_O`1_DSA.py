"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

"""

class AllOne:
    def __init__(self):
        # Maps each key to its current count
        self.count_map = {}
        # Maps each count to a set of keys having that count
        self.frequency_map = {}
        # Keep track of minimum and maximum counts
        self.min_count = None
        self.max_count = None

    def _add_to_frequency_map(self, key, count):
        """Add a key to the frequency map under the given count."""
        if count not in self.frequency_map:
            self.frequency_map[count] = set()
        self.frequency_map[count].add(key)

    def _remove_from_frequency_map(self, key, count):
        """Remove a key from the frequency map under the given count."""
        if count in self.frequency_map:
            self.frequency_map[count].discard(key)
            if not self.frequency_map[count]:
                del self.frequency_map[count]

    def inc(self, key: str) -> None:
        """Increment the count of the given key by 1."""
        if key in self.count_map:
            current_count = self.count_map[key]
            new_count = current_count + 1
            self.count_map[key] = new_count
            # Remove the key from the current count group and add it to the new count group
            self._remove_from_frequency_map(key, current_count)
            self._add_to_frequency_map(key, new_count)
        else:
            # If the key is not in the map, initialize it with count 1
            self.count_map[key] = 1
            self._add_to_frequency_map(key, 1)

        # Update min_count and max_count
        if self.min_count is None or self.min_count > self.count_map[key]:
            self.min_count = self.count_map[key]
        if self.max_count is None or self.max_count < self.count_map[key]:
            self.max_count = self.count_map[key]

    def dec(self, key: str) -> None:
        """Decrement the count of the given key by 1."""
        if key in self.count_map:
            current_count = self.count_map[key]
            new_count = current_count - 1

            # Remove the key if its count reaches zero
            if new_count == 0:
                del self.count_map[key]
                self._remove_from_frequency_map(key, current_count)
            else:
                # Update the key's count and frequency map
                self.count_map[key] = new_count
                self._remove_from_frequency_map(key, current_count)
                self._add_to_frequency_map(key, new_count)

            # Update min_count and max_count
            if not self.frequency_map:
                # If the frequency map is empty, reset min and max counts
                self.min_count = None
                self.max_count = None
            else:
                # Update min_count if necessary
                if current_count == self.min_count and current_count not in self.frequency_map:
                    self.min_count = min(self.frequency_map)

                # Update max_count if necessary
                if current_count == self.max_count and current_count not in self.frequency_map:
                    self.max_count = max(self.frequency_map)

    def getMaxKey(self) -> str:
        """Return one key with the maximum count."""
        if self.max_count is None:
            return ""
        return next(iter(self.frequency_map[self.max_count]))

    def getMinKey(self) -> str:
        """Return one key with the minimum count."""
        if self.min_count is None:
            return ""
        return next(iter(self.frequency_map[self.min_count]))


# Example usage:
allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
print(allOne.getMaxKey())  # Output: "hello"
print(allOne.getMinKey())  # Output: "hello"
allOne.inc("leet")
print(allOne.getMaxKey())  # Output: "hello"
print(allOne.getMinKey())  # Output: "leet"