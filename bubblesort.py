def bubbleSort(list):

    #크기 = 5
    length = len(list)

    for i in range(0, length -1):
    # -1은 마지막라운드까지 돌릴필요 없기때문
        for j in range(0, length -1 -i):
            if(list[j] > list[j + 1]):
                list[j],list[j+1] = list[j+1],list[j]


list = [5,1,4,2,8]
bubbleSort(list)
print(list)