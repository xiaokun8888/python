def is_pangram(s):
    s=s.lower()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c in s:
            i=1
        else:
            return False
    return True