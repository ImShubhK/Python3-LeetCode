<<<<<<< HEAD
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%3!=0:
            return False
        return Solution.isPowerOfThree(self,n//3)
=======
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%3!=0:
            return False
        return Solution.isPowerOfThree(self,n//3)
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        