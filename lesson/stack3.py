from pythonds.basic.stack import Stack
def parchecking(symbolstring):
    s=Stack()
    balanced=True
    index=0



    while index < len(symbolstring) and balanced :
        symbol =  symbolstring[index]

        if symbol == "(":
            s.push(symbol)


        elif symbol == ")":
            if "(" in s.items:
                if  s.peek()=="(" :
                    s.pop()
            else:
                balanced = False


        if symbol == "[":

            s.push(symbol)


        elif symbol == "]":
            if "[" in s.items:
                if s.peek() == "[":
                    s.pop()
            else: balanced =False


        if symbol == "{":
            s.push(symbol)


        elif symbol == "}":
            if "{" in s.items:
                if s.peek() == "{":
                    s.pop()
            else:
                balanced = False


        index=index+1

    if  balanced and s.isEmpty() :
        return True
    else:
        return False

print(parchecking(input()))




