list = [3,0,1,4,2,8,7,5]

def insertion_sort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while j>= 0 and list[j] > key:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
        
        print(list)

insertion_sort(list)