from pythonds.basic.stack import Stack
def infixtopostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opstack=Stack()
    postfixlist=[]
    print(infixexpr)
    tokenlist=infixexpr.split()
    print(tokenlist)
    for token in tokenlist:
        if token in "ABCDEFRGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            toptoken=opstack.pop()
            while toptoken != "(":
                postfixlist.append(toptoken)
                toptoken=opstack.pop()
        else:
            while (not opstack.isEmpty())and (prec[opstack.peek()]>=prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return ' '.join(postfixlist)


def  postfixeval(postfixexpr):
    operandstack= Stack()
    tokenlist =postfixexpr.split()

    for token in tokenlist:
        if token in "0123456789":
            operandstack.push(int(token))
        else:
            operand2=operandstack.pop()
            operand1=operandstack.pop()
            result=domath(token,operand1,operand2)
            operandstack.push(result)
    return operandstack.pop()
def domath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op =="/":
        return op1/op2
    elif op=="+":
        return op1+op2
    else:
        return op1-op2

a=infixtopostfix("2 / 3 + 3 * 5")
print(postfixeval(a))








