class function_1:
    def __init__(self, func):
        self.func=func
        self.state=[]
        a= self.func(10,20)
        print(a)
        
    def __call__(self, *agrs):
        a= self.func(*agrs)
        return a

    @classmethod
    def function_2(cls, func):
        return cls(func)

@function_1.function_2
def function_3(x, y):
    return x+y

print(function_3(20,30))


        