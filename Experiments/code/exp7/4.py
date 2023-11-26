from math import sqrt

class Vector:
    #Python 元组 tuple() 函数将列表转换为元组
    def __init__(self, it):
        self._v = tuple(x for x in it)

    # 把打印元组时的空格去掉
    def __str__(self):
        return str(self._v).replace(' ', '')
    
    # 检查两个向量是否长度相等    
    def check(self, other):
        if not len(self._v) == len(other._v):
            raise ValueError('Vectors of different length')
    
    #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    def add(self, other):
        self.check(other)
        return Vector(s + o for s, o in zip(self._v, other._v))

    def subtract(self, other):
        self.check(other)
        return Vector(s - o for s, o in zip(self._v, other._v))
    
    def dot(self, other):
        self.check(other)
        return sum(s*o for s, o in zip(self._v, other._v))
    
    def norm(self):
        return sqrt(sum(s**2 for s in self._v))
    
    def equals(self,other):
        return self._v==other._v