def find_senior(lst): 
    
    # 利用生成器作为max函数的参数，找到最大的年龄
    mage = max(a['age'] for a in lst)
    
    # 利用列表推导返回结果
    return [a for a in lst if a['age']==mage]