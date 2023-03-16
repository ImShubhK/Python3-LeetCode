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
            return False