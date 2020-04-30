#https://tech.ssut.me/understanding-python-metaclasses/
class ObjectCreator():
    pass

print(ObjectCreator)
my_object = ObjectCreator()
print(my_object)
# --> Class in python is a object that makes objects.

print(hasattr(ObjectCreator, 'test'))
ObjectCreator.test = lambda x : x
print(hasattr(ObjectCreator, 'test'))
print(ObjectCreator.test(1))

ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror)
print(id(ObjectCreatorMirror) == id (ObjectCreator))

MyClass = type('MyClass', (), {}) # type is MetaClass
print(MyClass)

str_test = "test"
print(str_test.__class__) # <class 'str'>
print(str_test.__class__.__class__) # <class 'type'>

