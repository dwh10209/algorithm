class Solution:
    def isAnagram(self, str1 : str, str2: str) -> bool:
        # sorted approach
        # pay attention to edge case
        if len(str1) != len(str2):
            return False
        # return sorted(str1) ==  sorted(str2)

        # hashmap approach
        counts, count = {}, {}

        for i in range(len(str1)):
            counts[str1[i]] = 1 + counts.get(str1[i], 0)
            count[str2[i]] = 1 + count.get(str2[i], 0)
        return counts == count
