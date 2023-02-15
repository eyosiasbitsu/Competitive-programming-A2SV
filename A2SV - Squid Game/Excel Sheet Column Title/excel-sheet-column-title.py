class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ''

        while columnNumber:
            res = res + chr(ord('A') + (columnNumber-1) % 26)
            columnNumber = (columnNumber -1 )//26

        return res[::-1]
