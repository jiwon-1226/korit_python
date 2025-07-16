#
# print(10/0)

try:
    print(10/0)
except:
    print("예외 발생")

try:
    num = int(input("숫자를 입력해주세요:"))
    print(10/num)
except ValueError: #값 데이터 오류
    print("문자말고 숫자 넣")
except ZeroDivisionError:
    print("0 넣지 마라")