<<<<<<< HEAD
class Solution:
    def fib(self, n: int) -> int:
         if (n==0 or n==1):
            return n
         else :
=======
class Solution:
    def fib(self, n: int) -> int:
         if (n==0 or n==1):
            return n
         else :
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
            return self.fib(n-1)+self.fib(n-2)