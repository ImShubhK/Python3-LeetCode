<<<<<<< HEAD
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst=[]
        for i in zip(*matrix):
            lst.append(i[::-1])
=======
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst=[]
        for i in zip(*matrix):
            lst.append(i[::-1])
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        matrix[:]=lst