#pivot을 기준으로 쪼개기
def division(list,low,high):

    #pivot 값 정하기
    pivot = list[high]

    #i는 피봇을 기준으로 list를 정렬해주는 역할

    i = low - 1

    #j를 통해서 list를 훑는다.
    for j in range(low,high):

        if list[j]<pivot:

            i = i + 1
            #swap
            list[i],list[j] = list[j],list[i]

        #마지막으로 pivot이 들어갈 위치를 바꿔준다.
    list[i+1],list[high] = list[high],list[i+1]

    return i + 1

def quickSort(list,low,high):

    #pivot이 알맞은 위치에 있어서 QuickSort를 실행해줘도 되는지 확인하는 부분

    if low < high :

        #pivot 기준으로 쪼개기 위해 pivot 위치를 가져온다.
        pivot_position = division(list,low,high)

        #왼쪽과 오른쪽 부분을 쪼개준다.
        quickSort(list,low,pivot_position - 1 )
        quickSort(list,pivot_position + 1,high)

list = [10,80,30,90,50,40,70]
n = len(list)
quickSort(list,0,n-1)

print(list)