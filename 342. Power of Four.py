<<<<<<< HEAD
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%4!=0:
            return False
        return Solution.isPowerOfFour(self,n//4)
        
=======
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%4!=0:
            return False
        return Solution.isPowerOfFour(self,n//4)
        
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
