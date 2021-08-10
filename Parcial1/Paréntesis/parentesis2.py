def parentesis():
    s = input("Input: ")
    check = []
    for i in s:
        if(i == ')' or i == ']'):
            if(not check):
                top = 'a'
            else:
                top = check.pop()
            if(top == '('):
                if(i != ')'):
                    return False
            elif(top == '['):
                if(i != ']'):
                    return False
            else:
                return False
        else:
            check.append(i)
    if(not check):
        return True
    return True 
print(parentesis())