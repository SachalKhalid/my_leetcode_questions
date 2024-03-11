class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = [0] * 26
        
        for c in s:
            char_map[ord(c) - ord('a')] += 1
        
        result = ''
        
        for c in order:
            result += c * char_map[ord(c) - ord('a')]
            char_map[ord(c) - ord('a')] = 0
        
        for i in range(26):
            result += chr(i + ord('a')) * char_map[i]
        
        return result
