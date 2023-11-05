def spin_words(sentence):
    # Your code goes here
    result=[]
    spinWords=sentence.split()
    for i in spinWords:
        if len(i)>=5 :
            result.append(i[::-1])
        else:
            result.append(i)
    result=" ".join(result)
    return result