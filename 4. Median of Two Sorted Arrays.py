class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = [] 
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                list.append(nums1[i])
                i += 1
            else:
                list.append(nums2[j])
                j += 1
        list = list + nums1[i:] + nums2[j:]
        size = len(list)
        return (list[size//2]) if size % 2 != 0 else (list[size//2 - 1] + list[(size//2)])/2 