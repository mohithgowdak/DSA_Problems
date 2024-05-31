class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            num1 = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num2  = nums[j]
                num3 = nums[k]

                sum = num1 + num2 + num3 
                if sum > 0:
                    k -= 1
                elif sum < 0: # since the nums is sorted the number more in j+1
                    j += 1
                else:
                    triplets.add((num1 , num2 ,num3))
                    j += 1
                    k -= 1
        return triplets