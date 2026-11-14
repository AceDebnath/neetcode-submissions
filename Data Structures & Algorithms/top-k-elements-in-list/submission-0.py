class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        result = []

        for _ in range(k):
            max_num = max(freq ,key = freq.get)
            result.append(max_num)
            del freq[max_num]
        
        return result