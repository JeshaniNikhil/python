l=[]
while True:
    a=int(input(
    '''
    1 Push
    2 Pop
    3 Peek
    4 display
    5 exit
    '''
    ))
    if a==1:
        n=input("Enter The Value")
        l.append(n)
        print(l)
    elif a==2:
        if len(l)==0:
            print("Empty Stack")
        p=l.pop()
        print(p)
        print(l)
    elif a==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("last stack value",l[-1])
    elif a==4:
        print(l)
    elif a==5:
        exit(0)
    else:
        print("Enter Valid Chioce")
