
def mergesort(list):

    #완전히 쪼개질 때 까지 돌리기
    if len(list) > 1:

        #중간을 기준으로 쪼개기
        mid = len(list)//2

        left = list[:mid]
        right = list[mid:]

        # 왼쪽,오른쪽 부분 쪼개기
        print("left:",left)
        mergesort(left)

        print("right:",right)
        mergesort(right)

        #합치는 과정
        i = 0 
        j = 0
        k = 0

        #임시 정렬
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        print("임시 정렬:",list)

        #왼쪽에 남은 항목 있을 때 정렬
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        #오른쪽에 남은 항목 있을 때 정렬
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print("최종 정렬:",list)

list = [35,33,12,65,22,5,11,2]
mergesort(list)
#최종 정렬: [2, 5, 11, 12, 22, 33, 35, 65]