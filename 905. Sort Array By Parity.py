class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenlist = [i for i in nums if i%2==0]
        oddlist = [i for i in nums if i%2!=0]
        return evenlist+oddlist