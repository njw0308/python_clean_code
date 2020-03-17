#1.
class context_manager():

    def __enter__(self):
        print("START")
        return "<RETURN DATA>"

    def __exit__(self, type, value, traceback):
        if traceback: # error 가 들어온 경우 다른 결과를 출력하게끔.
            print("ERROR OCCURED")
        else:    
            print("FINISH")
        

with context_manager() as cm_obj:
    print(cm_obj)
    print("WORKING")

with context_manager() as cm_obj:
    raise ValueError("ERROR")

#2.
import contextlib
@contextlib.contextmanager
def another_context_manager():
    try:
        print("START")
        yield '<RETURN DATA>'
    finally:
        print("FINISH")

with another_context_manager() as var:
    print(var)
    print("WORKING")

with another_context_manager() as var:
    raise ValueError("ERROR")

#3.
class subclass_context_manager(contextlib.ContextDecorator):
    
    def __enter__(self):
        print("START")
    
    def __exit__(self, type, value, traceback):
        if traceback:
            print("ERROR OCCURED")
        else:
            print("FINISH")

@subclass_context_manager()
def any():
    print("WORKING")

@subclass_context_manager()
def error_any():
    raise ValueError("ERROR")

any()
error_any()

