# https://learnandlearn.com/python-programming/python-how-to/python-function-arguments-mutable-and-immutable
def func(arg):
    arg += ' in function'
    print(arg)

immutable = 'abc'
func(immutable)
print(immutable)

mutable = list('hello')
func(mutable)
print(mutable)