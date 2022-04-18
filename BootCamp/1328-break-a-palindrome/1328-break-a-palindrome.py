class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        count = 1
        l = len(palindrome)
        str1 = ""
        if l == 1:
            return ""
        def is_pali(st):
            i = 0
            j = len(st) - 1
            while i <= j and st[i] == st[j]:
                i += 1
                j -= 1
            if i == j or j == i-1:
                return True
        if l%2 == 0:
            for i in palindrome:
                if count == 1 and i !="a":
                    str1 += "a"
                    count -= 1
                else:
                    str1 += i
            if is_pali(str1):
                return str1[:l - 1:] + "b"
        else:
            if palindrome[0] != "a":
                return "a" + palindrome[1:l:]
            if palindrome[l//2 + 1] != "a":
                return palindrome[:l//2+1:] + "a" + palindrome[l//2+2::]
            if palindrome[-1] == 'a':
                return palindrome[:l - 1:] + "b"
        return str1