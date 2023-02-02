class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        result = letter_logs + digit_logs

        return result
