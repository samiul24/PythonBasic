def decorator_x(func):
    def inner(a,b):
        print('Started')
        print('Ended')
        c= func(a,b)
        print(c)
    return inner


def say(x,y):
    return x/y

s= decorator_x(say)
s(10,2)