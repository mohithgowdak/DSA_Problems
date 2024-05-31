class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=[]
        for x in s:
            if x.isalpha() or x.isnumeric():
                y.append(x.lower())
        return y==y[::-1]


        