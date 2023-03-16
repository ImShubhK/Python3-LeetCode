<<<<<<< HEAD
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s =0
        e = len(nums)-1
        while s<e:
            mid = s+(e-s)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                s = mid+2
            else:
                e = mid
=======
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s =0
        e = len(nums)-1
        while s<e:
            mid = s+(e-s)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                s = mid+2
            else:
                e = mid
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        return nums[e]