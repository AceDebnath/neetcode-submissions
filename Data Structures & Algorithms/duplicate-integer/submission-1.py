class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preMap ={}
        for i,num in enumerate(nums):
            if num in preMap:
                return True
                break
            preMap[num] = i
            print(preMap)
        return False