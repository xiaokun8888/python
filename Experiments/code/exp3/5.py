def disemvowel(string_):
    
    return "".join(c for c in string_ if c.lower() not in "aeiou")