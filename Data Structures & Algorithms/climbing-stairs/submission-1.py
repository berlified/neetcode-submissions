class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two #new answer + move forward
            two = temp
        return one

# repeating this until we reach n, will give the answer