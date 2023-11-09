class Stack(list):
    def __init__(self):
        self.stack = list()
    
    def push(self, val):
        self.stack.append(val)
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()


def checkIfOperator(char):
    if char in "-+/*^":
        return True
    return False


def getOperatorPostion(operators, operator):
    for value in operators:
        if operator != None and operator in value:
            return operators.index(value)


def infixStringToList(infix):
    index = 0
    token = ""
    infixList = []
    for index, char in enumerate(infix):
        if checkIfOperator(char) or char in "()":
            if token != "": infixList.append(token)
            infixList.append(char)
            token = ""
        else:
            token+= char.strip()
            if index == len(infix)-1: infixList.append(token)

    return infixList


def infixToPostfix(infix):
    operatorStack = Stack()
    operators = ["-+", "/*", '^']
    postfixList = []
    countOpen, countClose = 0, 0
    infixList = infixStringToList(infix)

    for i, token in enumerate(infixList):
        if checkIfOperator(token) or token in "()":
            if token == "(": countOpen+=1
            elif token == ")": countClose+=1

            if i != len(infixList)-1 and token not in "()": 
                if checkIfOperator(infixList[i+1]): return None

            elif i == len(infixList)-1:
                if checkIfOperator(token): return None

            elif len(operatorStack.stack) == 0 or token == "(":
                operatorStack.push(token)

            elif token == ")":
                while operatorStack.top() != "(":
                    postfixList.append(operatorStack.pop())
                operatorStack.pop()

            else:
                topOperator = getOperatorPostion(operators, operatorStack.top())
                newOperator = getOperatorPostion(operators, token)

                while topOperator != None and newOperator <= topOperator:
                    postfixList.append(operatorStack.pop())
                    topOperator = getOperatorPostion(operators, operatorStack.top())

                operatorStack.push(token)

        elif token.isdigit():
            postfixList.append(token)

        elif token == " ": continue

        else: return None

    if countClose != countOpen: return None

    for index in range(len(operatorStack.stack)):
        postfixList.append(operatorStack.pop())

    return postfixList


def postfixEvaluation(postfix):
    postfixStack = Stack()

    for token in postfix:
        if checkIfOperator(token):
            a = postfixStack.pop()
            b = postfixStack.pop()
            if token == "/":
                postfixStack.push(eval(f"{b}//{a}"))
            else:
                postfixStack.push(eval(f"{b}{token}{a}"))
        else:
            postfixStack.push(token)

    return postfixStack.stack[0]


def main():
    infix = input("Enter infix notation : ")
    postfix = infixToPostfix(infix)

 
    print("\nPostfix Notation: ", end="")
    print(postfix)


main()

            