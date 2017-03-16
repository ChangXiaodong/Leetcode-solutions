import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hash_map.get(val, "Null") == "Null":
            self.hash_map[val] = val
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        return self.hash_map.pop(val, "Null") != "Null"

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.hash_map[random.sample(self.hash_map.keys(), 1)[0]]