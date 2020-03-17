import os

print(os.path.abspath(__file__)) # 현재 파일 위치

print(os.path.dirname(os.path.abspath(__file__))) # 현재 파일이 속한 폴더.