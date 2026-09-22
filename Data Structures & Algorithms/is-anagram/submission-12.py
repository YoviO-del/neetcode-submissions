from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Syntax issues: 
        # 1. looped through the range of len(s_hash) not s
        # 2. len(s_hash) instead of every key in s_hash
        # 3. Brackets should've been used instead of parentheses for index calling of a char for my string

        #check for extraneous solutions first
        if len(s) != len(t):
            return False
        
        # Didn't know syntax at first but used AI to find correct syntax
        # sort words so keys align up
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))

        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

       

        
        # Do this twice (once for each word)

        # Loop through each word
        # Map every character to a hashmap
        # The key would be the character and the value would the occurence

       
        for idx in range(len(s)):
            s_hash[new_s[idx]] += 1
            t_hash[new_t[idx]] += 1

        # Check the count 
        # As soon as they don't match return False
        for key in ((s_hash)):
            if s_hash[key] != t_hash[key]:
                return False

        # We are able to return true since it passes everything
        return True