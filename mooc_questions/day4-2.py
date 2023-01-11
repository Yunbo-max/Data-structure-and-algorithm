class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


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