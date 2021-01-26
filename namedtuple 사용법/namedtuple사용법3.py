#클래스로 구현한 방법
#데이터 두개를 엮기위해 클래스를 사용하는 것은 과분해보인다.
class FishShapedBun:

    def __init__(self, source, crispy):
        self.source = source
        self.crispy = crispy

def printFishes(fishes):
    for i, fish in enumerate(fishes):
        print(f"{i + 1}번째 붕어빵 - 재료:{fish.source}, 바삭함:{fish.crispy}")

fishes_data = [("팥", 1), ("바닐라", 5), ("바닐라", 4), ("팥", 8), ("팥", 9)]
fishes = [FishShapedBun(*data) for data in fishes_data]

print(fishes[1].crispy)

#4
crispy_fishes = [fish for fish in fishes if fish.crispy >= 5]
printFishes(crispy_fishes)