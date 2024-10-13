

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        j = 0
        
        for i in range(len(nums)):
            if nums[i] in count: # this is because the dictionar cant 
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
            # count[nums[i]] += 1 --> this dont work because you have to entry it before increment
            if count[nums[i]] <= 2:
                nums[j] = nums[i]
                j += 1

        return j
