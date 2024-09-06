class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        
        for c in tokens:
            match c:
                case "+":
                    myStack.append(myStack.pop() + myStack.pop())
                case "-":
                    x,y = myStack.pop(), myStack.pop()
                    myStack.append(y - x)
                case "*":
                    myStack.append(myStack.pop() * myStack.pop())
                case "/":
                    x,y = myStack.pop(), myStack.pop()
                    myStack.append(int(y / x))
                case _:
                    myStack.append(int(c))
                    
        return myStack[0]
                    
        