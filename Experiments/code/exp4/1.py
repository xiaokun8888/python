def naughty_or_nice(data):
    nt=0;
    nc=0
    for i in data.values():
        for j in i.values():
            if j=='Naughty':
                nt+=1
            else:
                nc+=1
    if nt>nc:
        return "Naughty!"
    else :
        return "Nice!"