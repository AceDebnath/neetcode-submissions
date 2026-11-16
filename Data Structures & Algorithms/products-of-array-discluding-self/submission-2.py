class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6
        n = len(nums)
        s = [1] *n


        prefix = 1
        for i in range(n):
            s[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            s[i] *= suffix
            suffix *= nums[i]

        return s
        