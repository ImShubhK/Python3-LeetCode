<<<<<<< HEAD
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n=nums[len(nums)-1]
            nums.pop()
=======
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n=nums[len(nums)-1]
            nums.pop()
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
            nums.insert(0,n)