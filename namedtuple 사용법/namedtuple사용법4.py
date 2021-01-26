#namedtuple로 구현한 방법
from collections import namedtuple

#namedtuple('사용할 클래스 이름', '들어갈 인자 띄어쓰기')
FishShapedBun = namedtuple('FishShapedBun', "source crispy")

def printFishes(fishes):
    for i, fish in enumerate(fishes):
        print(f"{i+1}번째 붕어빵 - 재료:{fish.source}, 바삭함:{fish.crispy}")

fishes_data = [("팥", 1), ("바닐라", 5), ("바닐라", 4), ("팥", 8), ("팥", 9)]
fishes = [FishShapedBun(*data) for data in fishes_data]

crispy_fishes = [fish for fish in fishes if fish.crispy >= 5]