class Event:
    """
    확장성을 가진 이벤트 시스템으로 리팩토링
    1. SystemMonitor 클래스를 추상적인 이벤트와 협력하도록 변경
    2. 이벤트에 대응하는 개별 로직은 각 이벤트 클래스에 위임.
    """
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

class SystemMonitor:

    def __init__(self, event_data):
        self.event_data = event_data
    
    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                print(event_cls)
                continue
        return UnknownEvent(self.event_data)

l1 = SystemMonitor({"before" : {"session" : 0}, "after" : {"session" : 1}})
l2 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 0}})
l3 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 1}})
print(l1.identify_event().__class__.__name__)
print(l2.identify_event().__class__.__name__)
print(l3.identify_event().__class__.__name__)
