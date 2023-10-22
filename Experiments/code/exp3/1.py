def solution(number):
    s=[]
    for i in range(1,number):
        if i%3==0 or i%5==0:
             s.append(i)
    return sum(s)
    #pass