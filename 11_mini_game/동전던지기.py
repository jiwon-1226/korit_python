import random
import time

coin_sides = ["앞면", "뒷면"]
user_wins = 0
computer_wins = 0
round_played = 0

print("동전 던지기 게임이 시작되었습니다.")
while True:
    print(f"===========round{round_played}============\n             =현재 전적=\n사용자 : {user_wins}, 컴퓨터 : {computer_wins}\n")


    user_guess = input("앞면과 뒷면 중 하나를 선택해주세요. (그만 하려면 '종료' 입력) :")
    if user_guess == "종료":
        print(f"================게임 종료===============\n최종 젅적 : 사용자 {user_wins}승, 컴퓨터 {computer_wins}승\n==========================")
        break

    if user_guess not in coin_sides:
        print("앞면, 뒷면 또는 종료 중 하나를 정확히 입력해주세요.")
        continue

    computer_guess = random.choice(coin_sides)
    print(f"컴퓨터는 {computer_guess}를 선택했습니다")
    time.sleep(1)

    print("\n동전을 던집니다")
    time.sleep(2)
    coin_result = random.choice(coin_sides)

    print(f"\n동전은 {coin_result}이(가) 나왔습니다")

    if user_guess == coin_result:
        print("예측 성공\n")
        user_wins += 1
    else:
        print("실패\n")

    if computer_guess == coin_result:
        computer_wins += 1


    round_played += 1
    if round_played >= 5:
        if user_wins >= 5:
            print(f"================게임 종료===============\n최종 전적 : 사용자 {user_wins}승, 컴퓨터 {computer_wins}승\n==========================\n컴퓨터를 이겼습니다. 굳")
        elif computer_wins >= 5:
            print(f"================게임 종료===============\n최종 전적 : 사용자 {user_wins}승, 컴퓨터 {computer_wins}승\n==========================\n컴퓨터가 이겼습니다. 분발하십쇼.")
        else:
            print(f"================게임 종료===============\n최종 전적 : 사용자 {user_wins}승, 컴퓨터 {computer_wins}승\n==========================\n다음엔 조금 더 잘해봅시다")
        break