class ComplicateNamespace:

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in ["id_", "user", "location"]:
                setattr(instance, key, value)
        
        return instance

cn = ComplicateNamespace.init_with_data(id_=12, user="jw", location="localhost.com", extra="excluded")

print(cn.id_, cn.user, cn.location)

print(hasattr(cn, "extra"))

class Namespace:

    def __init__(self, **data):
        accepted_data = {
            k: v for k, v in data.items() if k in ["id_", "user", "location"]
        }
        print(self.__dict__)
        self.__dict__.update(accepted_data)

n = Namespace(id_=12, user="jw", location="localhost.com", extra="excluded")

print(dir(Namespace))
print(dir(n))
print(n.__dict__)
print(n.id_, n.user, n.location)
