class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # put the prefix in array, suffix multiplied to it.

        res = [1] * (len(nums))         #if len=4 ([1,1,1,1])

        prefix = 1
        for i in range(len(nums)):         #iterate through the array
            res[i] = prefix
            prefix *= nums[i]              # update the prefix
            
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
