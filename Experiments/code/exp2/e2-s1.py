def nearest_sq(n):
    # pass
    if n<1:
        n=1
    else:
        no=n
        n=int(n**0.5)
        na=n**2
        nr=(n+1)**2
        if (no-na)<(nr-no):
            n=na
        else:
            n=nr
    return n