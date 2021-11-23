def selectSort(list):
    for i in range(len(list)-1):

        min_index = i

        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:

                min_index = j

        list[i], list[min_index] = list[min_index], list[i]
        
list = [64,25,12,22,11]
selectSort(list)
print(list)

#O(n^2)
#결과값 = [11, 12, 22, 25, 64]