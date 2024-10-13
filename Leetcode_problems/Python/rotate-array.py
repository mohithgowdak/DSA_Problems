class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        