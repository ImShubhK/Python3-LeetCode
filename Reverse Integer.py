class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        if num[0] == "-":
            rnum = int("-" + ''.join(num[1:][::-1]))
        else:
            rnum = int(''.join(num[::-1]))
        if rnum >= -2**31 and rnum <= 2**31 - 1:
            return rnum
        else:
            return 0