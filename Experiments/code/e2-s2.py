def bouncing_ball(h, bounce, window):
    i=1
    if h<=window or bounce>=1 or bounce<=0 or h<=0:
        return -1
    while h*bounce>window:
        h=h*bounce
        i+=2
    return i