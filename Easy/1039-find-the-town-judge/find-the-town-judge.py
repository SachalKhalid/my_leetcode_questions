class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        check_list = [0]*(n+1)
        for sublist in trust:
            first_elemnt = sublist[0]
            second_element = sublist[1]

            check_list[first_elemnt] -= 1
            check_list[second_element] += 1

        for check in range(1, n + 1):
            if check_list[check] == n-1:
                return check
        return -1
            
        