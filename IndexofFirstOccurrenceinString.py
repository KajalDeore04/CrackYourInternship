class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
                
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        for i in range(haystack_len - needle_len + 1):
            if haystack.startswith(needle, i):
                return i
                
        return -1
