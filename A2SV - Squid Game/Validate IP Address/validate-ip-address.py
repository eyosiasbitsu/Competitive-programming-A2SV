class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        arr_v4 = []
        arr_v6 = []

        if '.' in queryIP:
            arr_v4 = queryIP.split('.')

            if len(arr_v4) != 4:
                return "Neither"
            
            for a in arr_v4:
                if not a:
                    return "Neither"

                if a[0] == '0' and len(a) > 1:
                    return "Neither"

                for c in a:
                    if c not in "0123456789": 
                        return "Neither"

                if int(a) not in range(0, 256):
                    return "Neither"

            return "IPv4"

        else:
            arr_v6 = queryIP.split(':')

            if len(arr_v6) != 8:
                return "Neither"
            
            for c in arr_v6:
                if not c:
                    return "Neither"

                if len(c[0]) not in range(1,4):
                    return "Neither"

                if len(c) > 4:
                    return "Neither"

                for char in c:
                    if char not in "0123456789ABCDEFabcdef":
                        return "Neither"
                    
            return "IPv6"
