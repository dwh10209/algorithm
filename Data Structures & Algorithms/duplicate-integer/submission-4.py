class Solution:
    def hasDuplicate(self, num)-> bool:
        if len(set(num)) != len(num):
            return True
        return False