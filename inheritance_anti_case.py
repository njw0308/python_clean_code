import collections
from datetime import datetime
class TransactionPolicy(collections.UserDict):

    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

policy = TransactionPolicy({
    "client1": {
        "fee":1000,
        "expiration_data" : datetime(2020, 1, 3)
    }
})

print(policy["client1"])
print(dir(policy)) # 불필요한 메서드들이 상속되고 있음.