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
    
    # optimized approach - sliding window and two pointers
    def optimizedLengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        l = 0
        window = set()
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len

# Best approach removing the whole innter loop by keeping track of each character index
class Solution:
    def bestLengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        l = 0
        for r, ch in enumerate(s):
            if s[r] in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            last_seen[ch] = r
            max_len = max(max_len, r - l + 1)
        return max_len