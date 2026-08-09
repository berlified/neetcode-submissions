class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)         #dictionary with lists

        for s in strs:
            count = [0] * 26. #for 26 alphabets

            for c in s:
                count[ord(c) - ord("a")] += 1  #finding respective number for char

            res[tuple(count)].append(s)    
               
            #we are using tuples here because we need something with a single key & use it as dictionary keys

            # it then adds all the strings that produces the same tuple

        return list(res.values())