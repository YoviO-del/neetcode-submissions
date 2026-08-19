class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charList1 = list(s)
        charList2 = list(t)

        charList1.sort()
        charList2.sort()

        for i in range(len(s)):
            if charList1[i] != charList2[i]:
                return False
        
        return True

        # hashS, hashT = {}, {}

        # for i in range(len(s)):
        #     hashS[i] = s[i]
        #     hashT[i] = t[i]

        # dict(sorted(hashS.items()))
        # dict(sorted(hashT.items()))

        # for i in range(len(hashT)):
        #     if hashT[i] != hashS[i]:
        #         return False

        # return True