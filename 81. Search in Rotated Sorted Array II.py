class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return True
            if nums[l]<nums[mid]:
                if nums[l]<=target and nums[mid]>=target:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[l]>nums[mid]:
                if nums[mid]<=target and nums[r]>=target:
                    l=mid+1
                else:
                    r=mid-1
            else:
                l+=1
        return False