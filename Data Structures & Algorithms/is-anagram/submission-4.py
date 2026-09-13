class Solution:
    def isAnagram(self, str1 : string, str2: string) -> bool:
        # sorted approach
        return sorted(str1) ==  sorted(str2)
        