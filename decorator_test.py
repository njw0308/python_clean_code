def test_decorator(func):
    def function_wrapper(var):
        print("Before calling " + func.__name__)
        func(var)
        print("After calling " + func.__name__)
    return function_wrapper

def be_decorated(var):
    print("Hi, be_decorated func has been called with " + str(var))

be_decorated = test_decorator(be_decorated)
be_decorated("42")

@test_decorator
def be_decorated(var):
    print("Hi, be_decorated func has been called with " + str(var))

be_decorated("42")