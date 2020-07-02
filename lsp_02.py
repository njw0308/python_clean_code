class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data : dict):
        return False

    @staticmethod
    def meets_condition_pre(event_data : dict):
        """
        인터페이스 계약의 사전 조건
        """

        assert isinstance(event_data, dict) , f"{event_data} is not a dict"
        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)

class UnknownEvent(Event):
    """
    식별할 수 없는 이벤트
    """

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (event_data["before"].get('session') == 0 and \
            event_data["after"].get('session') == 1)

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data : dict):
        return (event_data["before"].get('session') == 1 and \
            event_data["after"].get('session') == 0)

class SystemMonitor:
    """시스템에서 발생한 이벤트"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.meets_condition_pre(self.event_data)
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnknownEvent,
        )
        return event_cls(self.event_data)

l1 = SystemMonitor({"before" : {"session" : 0}, "after" : {"session" : 1}})
l2 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 0}})
l3 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 1}})
print(l1.identify_event().__class__)
print(l2.identify_event())
print(l3.identify_event().__class__.__name__)

e1 = SystemMonitor("123")
e2 = SystemMonitor({"before" : {"session" : 0}, "test" : {"session" : 1}})
# print(e1.identify_event().__class__.__name__)
print(e2.identify_event().__class__.__name__)