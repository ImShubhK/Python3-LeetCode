<<<<<<< HEAD
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
=======
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        return nums[len(nums)//2]