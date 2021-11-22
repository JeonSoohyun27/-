from typing import DefaultDict


def insertSort(list):

    for i in range(1, len(list)):
        # 첫번째 항목은 비교대상이 아니기 때문에 1부터 시작
        key = list[i]

        j = i-1

        while j>=0 and key < list[j]:

            list[j+1] = list[j]

            j -= 1
        
        list[j+1] = key

list = [12,11,13,5,6]
insertSort(list)
print(list)

#결과값 = [5,6,11,12,13]
#O(n^2)