"""
* 좋은 코드를 작성하는 방법.
1. 이 코드를 동료 개발자가 쉽게 이해하고 따라갈 수 있는가?
2. 팀에 새로 합류하는 사람도 쉽게 이해하고 효과적으로 작업할 수 있는가?

--> continuous integration build 가 목표. 
--> Mypy, Pylint, flake8 같은 오픈 소스

"""
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
print(add('1', '2'))
