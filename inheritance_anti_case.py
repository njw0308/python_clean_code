import collections
from datetime import datetime
class TransactionPolicy(collections.UserDict):
    """
    Anti Case
    1. 잘못된 계층 구조.
    """
    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

policy = TransactionPolicy({
    "client1": {
        "fee":1000,
        "expiration_data" : datetime(2020, 1, 3)
    }
})

#print(policy["client1"])
#print(dir(policy)) # 불필요한 메서드들이 상속되고 있음.

class TransactionPolicy_two:
    """
    컴포지션을 활용한 해결책
    ( TransactionPolicy 자체가 사전이 되는 것이 아니라 사전을 활용하는 것. )
    1. 사전을 private 속성에 저장 ( _data )
    2. __getitem()__ 으로 사전의 프록시를 만들고
    3. 필요한 public 메서드를 추가적으로 구현
    """
    def __init__(self, policy_data, **extra_data):
        # self._data = policy_data
        self._data = {**policy_data}
        self._data.update(**extra_data)

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)
    
    def __getitem__(self, customer_id):
        return self._data[customer_id]
    
    def __len__(self):
        return len(self._data)

policy = TransactionPolicy_two({
    "client1": {
        "fee":1000,
        "expiration_data" : datetime(2020, 1, 3)
    },
    "client2" : {
        "fee" : 1234
    }
})

print(policy._data)
print(policy["client1"])
policy.change_in_policy("client1", fee=0)
print(policy["client1"])
print(dir(policy)) # 불필요한 메서드가 상속되지 않는다.