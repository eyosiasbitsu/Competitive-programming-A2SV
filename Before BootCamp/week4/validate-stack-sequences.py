class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        i = 0
        op = []
        while(j<len(popped)):
            if i < len(pushed) and op and op[-1] == popped[j]:
                op.pop()
                j+=1
                continue
            if i < len(pushed) and popped[j] != pushed[i]:
                op.append(pushed[i])
                i+=1
                continue
            if i < len(pushed) and popped[j] == pushed[i]:
                i+=1
                j+=1
                continue 
            if i == len(pushed) and popped[j] == op[-1]:
                op.pop()
                j+=1
                continue
            if j < len(popped) and i == len(pushed) and popped[j] != op[-1]:
                break
        return not op
                