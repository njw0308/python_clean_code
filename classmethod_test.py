class TestClassMethod():

    def nothing(self, a, b):
        return a + b

    @classmethod
    def test_classmethod(cls, a, b):
        return a + b

    @staticmethod
    def test_staticmethod(a, b):
        return a + b


print(TestClassMethod.nothing(None, 2, 3))
print(TestClassMethod().nothing(2, 3))

print(TestClassMethod.test_classmethod(2, 3))

print(TestClassMethod.test_staticmethod(2, 3)) # class 도 staticmethod 바로 호출 가능

test_instance = TestClassMethod()

print(test_instance.nothing(2, 3))

print(test_instance.test_classmethod(2, 3)) # instance 도 사용 가능 classmethod 사용 가능

print(test_instance.test_staticmethod(2, 3))

class Language():
    
    default_language = '한국어'

    def __init__(self):
        self.first_language = self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()
    
    def print_language(self):
        print(self.first_language)

class InheritLanguage(Language):
    default_language = 'English'

a = InheritLanguage.static_my_language() 
a.print_language() # 한국어  
# --> static 이라는 단어에서 알 수 있듯이 해당 class ( Language ) 와 연관 있는 함수를 모아놓은 것.

b = InheritLanguage.class_my_language()
b.print_language() # english 
# --> class 라는 단어에서 알 수 있듯이 해당 func 을 부른 class ( InheritLanguage ) 와 새로운 연관을 맺음.
# --> 소위 'Factory Method' 라 불림. cls can be any subclasses.