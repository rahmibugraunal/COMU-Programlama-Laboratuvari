#Selection Sort ile diziyi küçükten büyüğe doğru sıralama


def MySelectionSort(my_array):
    swap_number=0

    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_number=swap_number+1

    print("swap number: ",swap_number)
    return

my_arr=[30,24,76,56,25,80,94,42,71,74]
MySelectionSort(my_arr)
print(my_arr)

#------------------------------------------------------------------------
#Binary Search ile arama

def MyBinarySearch(MySortedArray,item):
    first=0
    last=len(MySortedArray)-1
    found=False
    s=0

    while first<=last and not found:
        midpoint=(first+last)//2
        print("First-Last : ",first,last)
        s=s+1
        if(MySortedArray[midpoint]==item):
            found=True
        else:
            if(item<MySortedArray[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
    return  found,midpoint,s

my_arrays_2=[63,17,34,50,44,38,29]
print(MyBinarySearch(my_arrays_2,50))
