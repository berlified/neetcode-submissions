class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ""     

        for c in s:
            if c.isalnum():     #alphanumeric
                newStr += c.lower()     #add this to new string
        return newStr == newStr[::-1]       #check is it is the same
