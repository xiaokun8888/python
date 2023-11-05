def find_outlier(integers):
    j=[]
    o=[]
    for i in integers:
        if i%2==0:
            j.append(i)
        else:
            o.append(i)
    if len(j)==1:
        return j[0]
    if len(o)==1:
        return o[0]