#튜플은 내부 데이터에 접근하려면 인덱스를 사용하는 수 밖에 없다.
# 이런 상황에서 어떻게 손쉽게 데이터에 접근하는 방법
# 1.다음 다섯 개의 붕어빵을 데이터로 가지고 있어주세요 > (팥, 1), (바닐라, 5), (바닐라, 4), (팥, 8), (팥, 9)
# 2.입력한 순서에서 세번째 붕어빵에 대한 정보를 출력하세요.
# 3.모든 붕어빵을 출력하세요.
# 4.바삭함이 5 미만인 붕어빵을 모두 삭제하고 다시 모든 붕어빵을 출력해보세요.


#기존의 방법
source = []
crispy = []

#1
source.extend(["팥", "바닐라", "바닐라", "팥", "팥"])
crispy.extend([1, 5, 4, 8, 9])

#2
print(f"세번째 붕어빵에 대한 정보 - 재료:{source[2]}, 바삭함:{crispy[2]}")

#3
print(f"--- 모든 붕어빵을 출력 ---")
for i in range(len(source)):
    print(f"{i+1}번째 붕어빵 - 재료:{source[i]}, 바삭함:{crispy[i]}")


#4
print(f"--- 바삭함이 5 미만인 붕어빵들을 삭제합니다. ---")
remove_idx = [i for i in range(len(crispy)) if crispy[i] < 5]
remove_idx.sort(reverse =True)
for i in remove_idx:
    source.pop(i)
    crispy.pop(i)