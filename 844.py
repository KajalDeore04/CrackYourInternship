class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return result
        
        return build(s) == build(t)
