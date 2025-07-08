#

word = "python"

for char in word:
    print(char)

for i in range(5):
    print(i) #i : 0부터 5개의 숫자의 값을 냄

for i in range(2, 10):
    print(i) #2-9까지 출력

for i in range(2, 10, 2):
    print(i) #2부터 10미만까지, 2씩 증가

for i in range(1, 10):
    print(i)
    if i == 5:
        print("i가 5입니다. 정지")
        break

for num in range(1, 10):
    if num == 5:
        continue
    print(num)

#실습문제
#1부터 100까지 짝수만 출력하기(range)

for num2 in range(1,101):
    if num2 % 2 != 0:
        continue
    print(num2)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

for i in range(2, 101, 2):
    print(i)

#리스트의 합 구하기
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("리스트의 합 : ", total)


#구구단
for dan in range(1, 10):
    for n in range(1, 10):
        print(f"{dan} X {n} = {dan * n}")


#평균구하기
scores = [80, 90, 75, 88, 92]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("평균점수는", average)

