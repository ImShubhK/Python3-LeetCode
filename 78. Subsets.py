<<<<<<< HEAD
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         n=len(nums)
         ans=[]
         def solve(idx,lst):
            if idx>=n:
                ans.append(lst)
                return 
            solve(idx+1,lst)                    
            solve(idx+1,lst+[nums[idx]])        
         solve(0,[])
=======
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         n=len(nums)
         ans=[]
         def solve(idx,lst):
            if idx>=n:
                ans.append(lst)
                return 
            solve(idx+1,lst)                    
            solve(idx+1,lst+[nums[idx]])        
         solve(0,[])
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
         return ans