<<<<<<< HEAD
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if len(str(nums[i]))%2==0:
                count+=1
=======
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if len(str(nums[i]))%2==0:
                count+=1
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        return count