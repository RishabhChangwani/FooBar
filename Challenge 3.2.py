def solution(x, y):
    ctr=-1
    x,y = int(x), int(y)
    if(not(x == y) or (x%2==0 and y%2==0)):
        if x == 1:
            return str(y-1)
        elif y == 1:
            return str(x-1)
        else:
            while(x>1 or y>1):
                if x <=0 or y<=0:
                    return("impossible")
                if x > y:
                    ctr+= x // y
                    x= x%y
                elif y > x:
                    ctr+= y//x
                    y=y%x
            return str(ctr)
    else:
        return "impossible"

print(solution("25","35"))