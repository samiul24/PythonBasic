def function_1(fun):
    print('I am a decorator')
    def wrapper(*args, **kwargs):
        a= fun(*args, **kwargs)
        return a
    return wrapper


def function_2(x,y):
    print('I am a addition function')
    z=x+y
    return z

d=function_1(function_2)
print(d(10,y=20))