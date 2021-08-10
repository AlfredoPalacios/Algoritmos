def parentesis():
    s = input("Input: ")
    check = []
    for i in s:
        if(i == '(' or i == '['):
            check.append(i)
        else:
            if not(len(check)):
                return False
            else:
                top = check.pop()
            if(top == '('):
                if(i != ')'):
                    return False
            elif(top == '['):
                if(i != ']'):
                    return False
    return True
print(parentesis())