def duplicate_encode(word):
    word = word.lower()  # 将字符串转换为小写
    s = []
    for i in range(len(word)):
        count = 0
        for j in range(len(word)):
            if word[i] == word[j]:
                count += 1
        if count == 1:
            s.append('(')
        else:
            s.append(')')
    return ''.join(s)  # 将列表转换为字符串并返回