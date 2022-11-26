def function_1(fun):
    print('I am a decorator')
    def wrapper(*args, **kwargs):
        a= fun(*args, **kwargs)
        return a
    return wrapper

@function_1
def function_2(x,y):
    print('I am a addition function')
    z=x+y
    return z

print(function_2(10,y=20))
