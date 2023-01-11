from pythonds.basic.stack import Stack
def divideby2(number,base):
    digits="0123456789ABCDEF"
    remstack=Stack()
    while number > 0:
        rem=number%base
        remstack.push(rem)
        number=number//base

    qstring = ""
    while not remstack.isEmpty():
        qstring+=digits[remstack.pop()]
    return qstring



print(divideby2(283,2))