<<<<<<< HEAD
class Solution:
    def check(self, nums: List[int]) -> bool:
        count =0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
        if nums[-1]>nums[0]:
            count+=1
        return count<=1   
=======
class Solution:
    def check(self, nums: List[int]) -> bool:
        count =0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
        if nums[-1]>nums[0]:
            count+=1
        return count<=1   
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
