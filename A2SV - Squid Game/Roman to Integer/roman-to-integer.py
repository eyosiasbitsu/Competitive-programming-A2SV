class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i = {
            'I':  1,
            'IV': 4,
            'V':  5,
            'IX': 9,
            'X':  10,
            'XL': 40,
            'L':  50,
            'XC': 90,
            'C':  100,
            'CD': 400,
            'D':  500,
            'CM': 900,
            'M':  1000
        }
        converted = 0
        
        for roman, integer in r_to_i.items():
            while s.endswith(roman):
                s = s.removesuffix(roman)
                converted += integer
        
        return converted
