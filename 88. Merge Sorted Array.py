<<<<<<< HEAD
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2[0:n]
        nums1.sort()
=======
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2[0:n]
        nums1.sort()
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        