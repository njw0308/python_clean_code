class Event:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @classmethod
    def meets_condition(cls, event_data : dict):
        return False

class UnknownEvent(Event):
    """
    식별할 수 없는 이벤트
    """

class LoginEvent(Event):
    @classmethod
    def meets_condition(cls, event_data : dict):
        return (event_data["before"]["session"] == 0 and \
            event_data["after"]["session"] == 1)

class LogoutEvent(Event):
    @classmethod
    def meets_condition(cls, event_data : dict):
        return (event_data["before"]["session"] == 1 and \
            event_data["after"]["session"] == 0)

class TransactinEvent(Event):
    """
    이벤트를 우리가 원하는 대로 확장할 수 있음.
    Event 클래스를 상속 받아서 meets_condition 만 입맛에 맞게 구현하면 된다.
    """
    @classmethod
    def meets_condition(cls, event_data : dict):
        return event_data["after"].get("transaction") is not None

class SystemMonitor:
    """
    TransactionEvent 가 추가됐어도 identify_event 는 전혀 수정되지 않았다.
    """
    def __init__(self, event_data):
        self.event_data = event_data
    
    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)

l1 = SystemMonitor({"before" : {"session" : 0}, "after" : {"session" : 1}})
l2 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 0}})
l3 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 1}})
l4 = SystemMonitor({"after" : {"transaction" : 1}})
print(l1.identify_event().__class__.__name__)
print(l2.identify_event().__class__.__name__)
print(l3.identify_event().__class__.__name__)
print(l4.identify_event().__class__.__name__)
