class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for a in s:
            if a in s_dict:
                s_dict[a] += 1
            else:
                s_dict[a] = 1
        for a in t:
            if a in t_dict:
                t_dict[a] += 1
            else:
                t_dict[a] = 1
        if len(t) != len(s):
            return False
        for key, value in s_dict.items():
            if key not in t_dict or t_dict[key] != s_dict[key]:
                return False

        return True
            



        