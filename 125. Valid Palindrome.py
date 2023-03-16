<<<<<<< HEAD
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        pelidrome=' '
        for i in s:
            if i.isalnum():
                pelidrome+=i
        temp=pelidrome.strip()

        if temp==temp[::-1]:
            return True
        else:
=======
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        pelidrome=' '
        for i in s:
            if i.isalnum():
                pelidrome+=i
        temp=pelidrome.strip()

        if temp==temp[::-1]:
            return True
        else:
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
            return False