class Event:
    
    def __init__(self, data):
        self.data = data 
    
    def meets_condition(self, event_data : dict) -> bool:
        return False


"""
LSP? 하위 클래스는 상위 클래스에서 정의학 계약을 따르도록 디자인.
--> 인터페이스 디자인. Dbc
"""
class LoginEvent(Event):
    """
    LSP 위반
    1. 파생 클래스가 부모 클래스에서 정의한 파라미터와 다른 타입을 사용
    --> 계층 구조의 다형성이 손상
    """
    def meets_condition(self, event_data : list) -> bool:
        return bool(event_data)

class LoginEvent2(Event):
    """
    LSP 위반.
    """
    def meets_condition(self, event_data : dict) -> str:
        return 'False'

class LoginEvent3(Event):

    def meets_condition(self, event_data : dict, override : bool) -> bool:
        if override:
            return True
        return False