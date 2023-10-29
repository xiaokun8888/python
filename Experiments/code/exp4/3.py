def protein(rna):
    # your code here
    a=[]
    for i in range(0,len(rna),3):
        c=rna[i:i+3]
        if c in PROTEIN_DICT.keys():
            if PROTEIN_DICT[c]!='Stop':
                a.append(PROTEIN_DICT[c])
            else:
                break
    return "".join(a)
            