class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        char_map = {}
        used_chars = set()
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in used_chars:
                    return False
                char_map[s[i]] = t[i]
                used_chars.add(t[i])
            elif char_map[s[i]] != t[i]:
                return False
        return True
