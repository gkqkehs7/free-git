#튜플로 구현한 방법

#1
fishes = [("팥", 1), ("바닐라", 5), ("바닐라", 4), ("팥", 8), ("팥", 9)]

#2
def printFishes(fishes):
    print(f"--- 모든 붕어빵을 출력 ---")
    for i, fish in enumerate(fishes):
        print(f"{i + 1}번째 붕어빵 - 재료:{fish[0]}, 바삭함:{fish[1]}")

#3
print(f"세번째 붕어빵에 대한 정보 - 재료:{fishes[2][0]}, 바삭함:{fishes[2][1]}")

#4
crispy_fishes = [fish for fish in fishes if fish[1] >= 5]
printFishes(crispy_fishes)
