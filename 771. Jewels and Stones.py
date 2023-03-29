class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(jewels)
        ans = 0
        for i in stones:
            ans += count[i]
        return ans 