class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __getattr__(self, attr):
        if attr.startswith('fallback_'):
            name = attr.replace('fallback_', '')
            return "[fallback resolved] {}".format(name)

        raise AttributeError(f"{self.__class__.__name__}에는 {attr} 속성이 없습니다.")

dyn = DynamicAttributes("value")
print(dyn.attribute)

print(dyn.fallback_test)
try:
    print(dyn.nothing)
except Exception as e:
    print(e)
print(getattr(dyn, 'nothing', 'default_value')) # attributeError 가 발생할 때의 default value 를 지정.