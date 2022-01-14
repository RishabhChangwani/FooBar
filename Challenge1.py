def solution(data,n):
    dict = {}
    if(len(data)<101):
        for x in data:
            dict[x] = dict.get(x, 0) + 1
        return (i for i in data if dict[i] <= n)
