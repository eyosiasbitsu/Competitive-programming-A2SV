class Solution:
    def numberToWords(self, num: int) -> str:

        under_twenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        tens = ['','', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        chunks = ['Thousand', 'Million', 'Billion']

        temp = self.toWords(num, chunks, tens, under_twenty)
        result = ' '.join(temp)

        return result or 'Zero'
    
    
    def toWords(self, num, chunks, tens, under_twenty):
        if num == 0:
            return []

        if num < 20:
            return [under_twenty[num]]
        
        if num < 100:
            return [tens[num//10]] + self.toWords(num%10, chunks, tens, under_twenty)
        
        if num < 1000:
            quotient, remainder = num // 100, num % 100
            return [under_twenty[quotient], 'Hundred'] + self.toWords(remainder, chunks, tens, under_twenty)
        
        for power, chunk in enumerate(chunks, 1):
            if num < 1000 **(power + 1):
                quotient, remainder = num // 1000 **power, num % 1000 ** power
                return self.toWords(quotient, chunks, tens, under_twenty) + [chunk] + self.toWords(remainder, chunks, tens, under_twenty)
    
