X = int(input())
stick = [64]

if X == 64:
    print(1)
else:
    while(1):
        tmp = stick[-1]
        stick.remove(tmp)
        for i in range(2):
            stick.append(tmp//2)    


        if sum(stick[:-1]) > X:
            tmp1 = stick[-1]
            stick.remove(tmp1)
            
        else:
            if sum(stick) == X:
                print(len(stick)-2)
                break
            continue