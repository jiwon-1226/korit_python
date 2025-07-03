#세트
from pdb import line_prefix
from platform import java_ver

fruits = {"사가", "바나나", "ㅇ렌지", "바나나"}
print(fruits)
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers) #중ㅂㄱ은 제거

empty_dit = {} #빈 딕셔너리 형태

empty_set = set() #빈 세트

#욧 ㅜ가
s = {1, 2, 3}
s.add(4) #한 개만 ㅜ가 할때
print(s)

s.update([5, 6, 7]) #여러개 한 번에 ㅜ가
print(s)

#욧 삭제
# s.remove(9) #ㅈㄴ재하지 않는 값 제거 ㅇ류 발생
s.discard(10) #ㅈㄴ재하지 않는 값 제거 ㅇ류 없음
print(s)

s.clear()
print(s)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B) #중ㅂㄱ 제거, 합집합
print(A.union(B))

print(A & B) #교집합
print(A.intersection(B))

print(A - B) #타집합
print(A.difference(B))

#실습
pyton_lass = {"ㅓㄹ수", "영희", "민수", "지수"}
java_lass = {"영희", "민수", "지훈", "길ㄷㅇ"}

#ㅏ이썬가 자바 수업을 듣는 사람
print("둘다 듣는 사람 : ", pyton_lass.intersection(java_lass))
#ㅏ이썬만 듣는 사람
print("파이썬만 듣는 사람 : ", pyton_lass - java_lass)
#자바만 듣는 사람
print("자바만 듣는 사람 : ", java_lass - pyton_lass)
