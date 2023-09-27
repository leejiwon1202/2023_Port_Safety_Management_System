import sys
import numpy
print(1111111111111)
print(sys.argv[1])
print(sys.argv[3])
print(sys.argv[5])
print(2222222222222)
numbers = sys.argv[1].strip('()').split(',')
# 문자열에서 추출한 숫자를 정수로 변환하고 튜플로 만들기
result_tuple = tuple(int(num) for num in numbers)
