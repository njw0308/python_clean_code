class SystemMonitor:
    """
    SRP(Single Responsibility Principle) Anti Case
    """
    def load_activity(self):
        return None

    def identify_event(self):
        return None

    def stream_events(self):
        return None

"""
1. 독립적인 동작을 하는 메서드를 하나의 인터페이스에 정의했다는 점.
2. 그 결과 메서드마다 다양한 변경의 필요성이 생겨서 유지보수를 어렵게 한다.
"""


class AlertSystem:
    """
    SRP - 각 클래스마다 "단일 책임"을 갖게 하자.
    """
    def run(self):
        return None

class ActivityReader:

    def load(self):
        return None

class SystemMonitor:
    
    def identify_event(self):
        return None

class Output:

    def stream(self):
        return None
