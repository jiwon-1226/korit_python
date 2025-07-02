#입력받기
#input()
# a = input()
# print("내가 입력한 것 : " + a)

# username = input("이름을 입력하세요 : ")
# print("사용자 이름 : " + username)

# age = input("나이를 입력하세요 : ")
# print(type(age))
# print("사용자 나이 : " + age)
#input()으로 입력받은 모든 값은 모두 문자열(str) 형태이다.

# #출력하기 다양한 방식
# last_name = "김" #문자열 str
# first_name = "지원"
# name = last_name + first_name
# age = 21 #int
# phone_number = "01012345678" #숫자는 맨 앞에 0이 나올 수 없다.

# print("hi" + "hello" + "world")
# print("hi", "hello", "world")
# print("내 전화번호는 " + phone_number + "입니다.")
# print("제 나이는 " + age + "입니다.")
# print("제 나이는 {} 입니다.".format(age)) #옛날 방식, format의 문자열을 중괄호 안에 넣어라
# print("제 이름은 {}, 나이는 {} 입니다.".format(name, age)) #순서를 지킬 것
# print("제 이름은 {nm}, 나이는 {ag} 입니다.".format(nm="홍길동", ag=18))

# print(f"제 나이는 {age} 입니다") #f-string 방식

# print("제 나이는 %s 입니다" % age) #%s중 s->문자열 형태로 바뀜(잘 안씀) #모든 문자를 문자열로 포맷팅해서 출력
# print("제 나이는 %d 입니다." % age) #모든 문자를 정수형으로 포맷팅해서 출력
# print("제 이름은 %s 이고, 제 나이는 %d 입니다." % (name, age))
# # print("Loading...%d% " % 98) (x)
# print("Loading...%d%% " % 98) #%를 기호로 쓸 때, % 한 번 더 쓰기


# print("%10s" % "hi") #hi를 포함한 칸 수=10 문자열 포함 길이(문자열 앞 공백 포함)
# print("%-10s" % "hell0") #문자열 포함 길이(문자열 뒤 공백 포함)
# print("%0.4f" % 3.42215685) #앞의 0은 자리수를 의미. .4는 소수점 4번째 자리까지 표현
# print("%10.4f" % 3.42215685)  #10은 자리수를 의미하므로 소수점 4번째 자리까지 표현후 남는 자리만큼 앞에 공백

"""
%s => 문자열
%c => 문자 1개
%d => 정수
%f => 실수
%o => 8진수
%x => 16진수
%% => 리터럴 (문자 % 자체)
"""

#실습
# 이름 :
# 나이 :
#취미 :
#주소 :
#각각 변수에 넣고 f-string 방식으로 출력
#제 이름은 *이고, 제 나이는 *살 입니다. 제 취미는 *이고 주소는 *입니다.

myname = input("이름을 입력하세요 : ")
myage = input("나이를 입력하세요 : ")
myhobby = input("취미를 입력하세요 : ")
myhome = input("주소를 입력하세요 : ")
print(f"제 이름은 {myname}이고, 제 나이는 {myage}살 입니다. 제 취미는 {myhobby}이고 주소는 {myhome}입니다.")

#풀이
name = input("이름 : ")
age = input("나이 : ")
hobby = input("취미 : ")
adress = input("주소 : ")
print(f"제 이름은 {name}이고, 제 나이는 {age}살 입니다. \n제 취미는 {hobby}이고 주소는 {adress}입니다.")