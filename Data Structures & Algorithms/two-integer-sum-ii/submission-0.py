class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}

        for i,num in enumerate(numbers):
            res = target - num

            if res in s:
                if s[res] > i:
                    continue 
                else:
                    return [s[res] + 1,i +1]

            s[num] = i

        return []
        