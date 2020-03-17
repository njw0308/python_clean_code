"""
프로퍼티(property) - 객체의 어떤 속성에 접근을 제어하려고 할 때 사용
--> 속성 값을 가져오거나 수정하려고 할 때 property 를 생각해보자.
@property : 무언가에 응답하기 위한 쿼리
@<property_name>.setter : 무언가를 하기 위한 쿼리

getter --> access the private value from a class.
setter --> set the value to private attributes in a class
"""
class SampleClass:

    def __init__(self, a):
        self.__a = a
    
    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

obj = SampleClass(10)
print(obj.get_a()) # 10
obj.set_a(1)
print(obj.get_a()) # 1 
print(obj.__dict__) # {'_SampleClass__a': 1} 

class PropertySampleClass:

    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, var):
        self._a = var

obj = PropertySampleClass(10)
print(obj.a) # 10
obj.a = 5
print(obj.a) # 5 
print(obj.__dict__) # {'_a': 5}