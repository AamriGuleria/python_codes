class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            unique_set = set()              
            for j in range(i, n):
                if s[j] in unique_set:     
                    break
                unique_set.add(s[j])   
                max_len = max(max_len, len(unique_set)) 
        return max_len