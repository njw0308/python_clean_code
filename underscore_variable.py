"""
https://dbader.org/blog/meaning-of-underscores-in-python

1. single leading underscore : _var --> 'internal use' , but not force 
2. single trailing underscore : var_ --> avoid naming conflicts with python keyword
3. double leading underscore : __var --> 'name mangling'
4. double leading and trailing underscore : __var__ --> magic method
5. single underscore : _ --> "don't care"
"""

class Connector:

    def __init__(self, source):
        self.source = source
        self._timeout = 60 # _timeout 은 이 Connector 자체에서만 사용할 것이고, 호출자가 이 속성에 접근하지 않았으면 좋겠음!
    

conn = Connector('test')
print(conn.source)
print(conn._timeout)
print(conn.__dict__)

class Connector_v2:
    
    def __init__(self, source):
        self.source = source
        self.__timeout = 60
    
    def connect(self):
        print("my timeout is {} second".format(self.__timeout))
    
conn = Connector_v2("test")
print(conn.source)
print(conn.connect())
print(conn.__dict__)
print(conn._Connector_v2__timeout) # name mangling
print(conn.__timeout) # error
