"""
다중상속
"""
class BaseModule:
    module_name = "base"

    def __init__(self, module_name):
        self.name = module_name
    
    def __str__(self):
        return f"{self.module_name}:{self.name}"

class BaseModule1(BaseModule):
    module_name = "module-1"

class BaseModule2(BaseModule):
    module_name = "module-2"

class BaseModule3(BaseModule):
    module_name = "module-3"

class ConcreteModuleA12(BaseModule1, BaseModule2):
    """1과 2 확장"""

class ConcreteModuleB23(BaseModule2, BaseModule3):
    """2와 3 확장"""

print(BaseModule1("BaseModule1"))
print(BaseModule2("BaseModule2"))
print(BaseModule3("BaseModule3"))

print(ConcreteModuleA12("ConcreteModuleA12")) # module-1:ConcreteModuleA12
print(ConcreteModuleB23("ConcreteModuleB23")) # module-2:ConcreteModuleB23

# Python 은 MRO 알고리즘을 사용하여 메서드가 호출되는 방식을 정의하고 있음. 
# --> 메서드가 계층 구조에서 어떻게 해결되는지 알 수 있는 단서
print([cls.__name__ for cls in ConcreteModuleA12.mro()])

"""
믹스인(MixIn) : 코드를 재사용하기 위해 일반적인 행동을 캡슐화 해놓은 것
보통 다른 클래스와 함게 믹스인 클래스를 다중 상속하여 믹스인에 있는 메서드나 속성을 사용한다.
"""
class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token
    
    def __iter__(self):
        print("BaseTokenizer")
        yield  from self.str_token.split('-')

tk = BaseTokenizer('a-b-c-d')
print(list(tk))

class UpperIterableMixIn:
    def __iter__(self):
        print("UpperIterableMixIn")
        return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixIn, BaseTokenizer):
    pass

tk2 = Tokenizer('a-b-c-d')
# MixIn 에서 __iter__를 먼저 호출하고, 다시 super() 호출을 통해 다음 클래스 BaseTokenizer 에 위임한다. 
# --> 이 때 이미 대문자를 전달하게 됨.
print(list(tk2)) 
list_ = [3,2,1]
print(sorted(list_), list_)
