<<<<<<< HEAD
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
=======
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
>>>>>>> 26b14c934091522be0fc2cf18fe4aa7bdaa8714c
        return max(len(word.split()) for word in sentences)