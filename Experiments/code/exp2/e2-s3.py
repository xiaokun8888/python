def get_count(sentence):
    i=0
    for sen in sentence:
        if sen=='a'or sen=='e'or sen=='i'or sen=='o'or sen=='u':
            i+=1
    return i