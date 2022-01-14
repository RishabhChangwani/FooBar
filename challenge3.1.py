def findXOR(n):
    mod = n % 4
 
    if (mod == 0):
        return n
    elif (mod == 1):
        return 1
    elif (mod == 2):
        return n + 1
    elif (mod == 3):
        return 0
def findXORFun(l, r):
    return ((findXOR(l - 1) ^ findXOR(r)))

def solution(start, length):
    if start >=0 and start + length**2 <= 2000000000 and length > 0:
        xor_list = 0
        for i in range(length):
            istart = start+(i*length)
            iend = istart+(length - 1 - i)
            xor_list = xor_list^(findXORFun(istart,iend))
        return xor_list
