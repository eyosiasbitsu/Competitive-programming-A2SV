class Solution:
    def reverseParentheses(self, s: str) -> str: 
        strarr = []
        for i in s:
            strarr.append(i)
        
        list1 = []
        list2 = []
        for i in range (len(strarr)):
            if strarr[i] == '(':
                list1.append(strarr[i])
                list2.append(i)
            elif strarr[i] == ')':
                strarr[list2[-1]:i:1] = strarr[i:list2[-1]:-1]
                strarr[list2[-1]] = '.'
                strarr[i] = '.'
                list1.pop()
                list2.pop()             
            else:
                continue
        list3 = []
        for i in strarr:
            if i!=')' and i != '(' and i!= '.':
                list3.append(i)
        result = "".join(list3)
        return result