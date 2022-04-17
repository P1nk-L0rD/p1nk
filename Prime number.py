aboba = 1
while aboba ==1:
    x = int(input('Number: '))

    for y in range(2,1000):
        if x>y:
            z=x%y
            if z != 0:
                continue
            elif z==0:
                print('False')
                break
        elif x>=y:
            print('True')
            break
