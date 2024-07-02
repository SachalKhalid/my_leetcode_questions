class Solution:
    def threeConsecutiveOdds(self, arr):
        odds = 0
        for num in arr:
            odds = odds + 1 if num % 2 == 1 else 0
            if odds == 3:
                return True
        return False