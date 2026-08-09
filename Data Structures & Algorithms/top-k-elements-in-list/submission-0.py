class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}      #empty dictionary
        freq = [[] for i in range(len(nums) + 1)]   # n number of empty lists

        for n in nums:
            count[n] = count.get(n, 0) + 1      # count of n
        for n, c in count.items():              # store count + key in freq
            freq[c].append(n)

        res = []                                # res 
        for i in range(len(freq) -1, 0, -1):    # go reverse in freq
            for n in freq[i]:                   
                res.append(n)                   # append n in the res
                if len(res) == k:               # if n == k, return
                    return res