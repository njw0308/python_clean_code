class Event:
    """
    Openclosed ANTI CASE
    1. 이벤트 유형을 결정하는 논리가 일체형으로 중앙 집중화 된다.
    2. 새로운 유형의 이벤트를 추가할 때마다 메서드를 수정해야 한다. ( -> 수정에 닫히지 않은 상태 )
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data

class UnknownEvent(Event):
    """
    식별 불가 이벤트
    """

class LoginEvent(Event):
    """
    로그인 사용자에 의한 이벤트
    """

class LogoutEvent(Event):
    """
    로그아웃 사용자에 의한 이벤트
    """

class SystemMonitor:
    """
    구체 클래스와 직접 상호 작용하려는 형태. 
    -> 그 결과 메서드 수정이 빈번함.
    """
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if (self.event_data["before"]["session"] == 0 and \
            self.event_data["after"]["session"] == 1) :
            return LoginEvent(self.event_data)
        elif (self.event_data["before"]["session"] == 1 and \
            self.event_data["after"]["session"] == 0) :
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)

l1 = SystemMonitor({"before" : {"session" : 0}, "after" : {"session" : 1}})
l2 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 0}})
l3 = SystemMonitor({"before" : {"session" : 1}, "after" : {"session" : 1}})
print(l1.identify_event().__class__.__name__)
print(l2.identify_event().__class__.__name__)
print(l3.identify_event().__class__.__name__)
             

