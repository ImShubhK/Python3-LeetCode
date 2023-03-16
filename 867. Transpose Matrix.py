<<<<<<< HEAD
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
         m,n=len(matrix),len(matrix[0])
         ans = [[None] * m for _ in range(n)]
         for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        
=======
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
         m,n=len(matrix),len(matrix[0])
         ans = [[None] * m for _ in range(n)]
         for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
         return ans