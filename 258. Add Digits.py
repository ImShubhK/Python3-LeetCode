<<<<<<< HEAD
class Solution:
    def addDigits(self, num: int) -> int:
        if num ==0:
            return 0
        elif num%9==0:
            return 9
        else:
=======
class Solution:
    def addDigits(self, num: int) -> int:
        if num ==0:
            return 0
        elif num%9==0:
            return 9
        else:
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
            return (num%9)