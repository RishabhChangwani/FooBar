def solution(xs):
    if len(xs) < 51 or len(xs) > 0:
        power_output = 1
        max_negative = -1001
        count_0 = 0
        count_negative = 0
        for i in xs:
            if abs(i)>1000:
                return
            if i > 0:
                power_output*=i
            elif i<0:
                max_negative = max(max_negative,i) 
                power_output = power_output* i
            else:
                count_0+=1
        if (power_output < 0 and count_0 > 0 and count_0 == len(xs)-1) or count_0 == len(xs):
            return str(0)
        if power_output < 0 and len(xs) > 1:
            power_output = power_output//max_negative
            
        return str(power_output)