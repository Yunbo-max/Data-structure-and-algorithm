from pythonds.basic.stack import Stack
def  postfixeval(postfixexpr):
    operandstack= Stack()
    tokenlist =list(postfixexpr)

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

print(postfixeval("456*+"))