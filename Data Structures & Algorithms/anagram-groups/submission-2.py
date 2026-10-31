class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so we can solve it in two ways 
        d = {}

        for word in strs:
            key = ''.join(sorted(word))
            

            if key not in d:
                d[key] = []
        
            d[key].append(word)


        return list(d.values())