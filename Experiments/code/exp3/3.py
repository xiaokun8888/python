def valid_braces(string):
    braces={"(":")","[":"]","{":"}"}
    s=[]
    for i in string:
        if i in braces.keys():
            s.append(i)
        else :
            if len(s)==0 or i!=braces[s.pop()]:
                return False
    return len(s)==0