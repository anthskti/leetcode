class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        n = len(digits)
        for i, v in enumerate(digits):
            total += (10**(n - i-1)) * v

        total +=1
        res = []
        while total != 0:
            res.append(total % 10)
            total = total // 10

        return res[::-1]
        