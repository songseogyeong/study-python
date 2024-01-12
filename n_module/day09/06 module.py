import os
import sys

print(sys.path)
# 문자열 값으로 출력
print(os.path.abspath(os.path.dirname(__file__)))
print(sys.path.append(os.path.abspath(os.path.dirname(__file__))))