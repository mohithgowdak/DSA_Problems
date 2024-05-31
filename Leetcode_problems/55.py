class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''if len(nums)==1:
            return True
        goal=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:# greater than because goal is we have maximum jump
                goal=i
        return True if goal == 0 else False'''


        '''1) nums value represents max jump fromthat position
           2) Solving this using greedy method
           3) By using brute force were calculating all the possible jump from that position,
               by using recursion. Time complexity is around n^n
           4) Greedy optimizes for O(n) time complexity
           5) Hence in this soln index having 0 value should be reduced and also the path leading to index 
              having 0 should be reduced.
           6) we will be moving goal -> start position'''
        gas = 0
        for i in nums:
            if gas < 0:
                return False
            elif i > gas:
                gas = i
            gas -= 1
            
        return True

           


        