class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        n = len(s)
        max_count = 0
        max_freq = 0
        for r in range(n):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])
            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            max_count = max(max_count, r - l + 1)
        return max_count
