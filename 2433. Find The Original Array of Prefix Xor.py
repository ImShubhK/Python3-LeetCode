class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        return [p[0]] +[p[i]^p[i-1]for i in range(1,len(p))]