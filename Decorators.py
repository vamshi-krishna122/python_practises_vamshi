
def dec1(func):
    def wrap(*args, **kwargs):
        print("Decorator1 before Function Call")
        func(*args, **kwargs)
        print("Decorator1 after Function Call")
    return wrap

def dec2(func):
    def wrap(*args, **kwargs):
        print("Decorator2 before Function Call")
        func(*args, **kwargs)
        print("Decorator2 after Function Call")
    return wrap

def dec3(func):
    def wrap(*args, **kwargs):
        print("Decorator3 before Function Call")
        func(*args, **kwargs)
        print("Decorator3 after Function Call")
    return wrap

@dec1
@dec2
@dec3
def add(a, b):
    print(a + b)

add(3, 7)



def decorator_with_param(num):   
    def decorator(func):              
        def wrapper(a, b):
            result = num + func(a, b)
            print(result)
        return wrapper
    return decorator

@decorator_with_param(10)
def add(x, y):
    return x + y

add(5, 7)
