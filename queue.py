l = []
while True:
    a = int(input(
        '''
        1 for enqueue
        2 for dequeue
        3 for first
        4 last 
        5 exit
        '''
    ))
    if a == 1:
            n = int(input('Enter value'))
            l.append(n)
    elif a == 2:
        if len(l)==0:
            print("queue underflow")
        else:
            del l[0]
            print('dequeue success')
            print(l)
    elif a == 3:
        print(l[0])
    elif a == 4:
        length=len(l) - 1
        print(l[length])
    elif a == 5:
        exit(0)
    else:
        print('invalid operation')
