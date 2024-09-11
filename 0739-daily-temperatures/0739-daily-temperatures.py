class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        answer = [0]*n
        stack = []
        
        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = i - stack_index
            
            stack.append((t,i))
        
        return answer