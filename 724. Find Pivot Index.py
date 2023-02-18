class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lsum=0
        rsum=sum(nums)
        for i in range(n):
            rsum-=nums[i]
            if rsum==lsum:
                return i
            lsum+=nums[i]
        return -1