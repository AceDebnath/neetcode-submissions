class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # s = {}

        # for i,num in enumerate(numbers):
        #     res = target - num

        #     if res in s:
        #         if s[res] > i:
        #             continue 
        #         else:
        #             return [s[res] + 1,i +1]

        #     s[num] = i

        # return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left]+numbers[right]
            if total == target:
                return [left + 1,right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
            


        