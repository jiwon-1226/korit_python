#사용자 정의 함수
#기본적인 사용자 정의 함수
# def hello():
#     print("반갑습니다.")
#
# hello()
# hello()
# hello()


# def plus(num1, num2):
#     print(num1 + num2)
#
# plus(1, 3)
# plus(10, 50)

# def hello(name):
#     print(f"안녕하세요. {name}님")
#
# hello("홍길동")

# def hello(name="홍길동"):
#     print(f"안녕하세요. {name}님") # ="~" 기본 값 설정해두기
#
# hello()

#이름과 나이를 매개변수로 전달, 출력
#안녕하세요 제 이름은 ***이고 나이는 **입니다.

# def introduce(name="***", age="**"):
#     print(f"안녕하세요 제 이름은 {name}이고 나이는 {age}살 입니다.")
#
# introduce()

# 리턴값이 있는 사용자 정의 함수
# def plus(x, y):
#     return x + y
# result = plus(5, 8)
# print(result)
#
# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(6))
# print(multiple_seven(100))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(15))

#평균값
# def cal_average(score_list):
#     total = sum(score_list)
#     return round(total / len(score_list))
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 98, 85]
# score_list3 = [40, 90, 70]
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))
#
# #매개변수로 단 숫자를 전달하면 해당 구구단 출력하기
# def rnrneks(dan=1):
#     for d in range(dan,dan+1):
#         for n in range(1, 10):
#             print(f"{d} X {n} = ", d * n)
#
# rnrneks(7)
#
# def gugudan(num):
#     for i in range(1, 10):
#         print(f"{num} X {i} = {num * i}")
# gugudan(4)

#콜백 함수
#함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
#어떤 함수가 실해되는 동안 밀 정의된 다른 함수를 호출하여 실해앟느 역할
def calculator(x, y, operation):
    return operation(x, y)

def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiple(x, y):
    return x * y
def divide(x, y):
    return x / y

print(calculator(5, 6, plus))
print(calculator(40, 5, minus))


import time

def timer(pause_second, callback):
    print(f"{pause_second}초 타이머가 시작되었습니다")
    print(f"{pause_second}초 뒤에 함수가 실행됩니다")

    time.sleep(pause_second)

    callback()
    print("타이머가 종료되었습니다")

def hello():
    print("안녕하세요")

timer(5, hello)








