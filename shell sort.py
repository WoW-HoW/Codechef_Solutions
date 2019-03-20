def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2

    while gap > 0:
 
        for i in range(gap,n):
 
            temp = arr[i]
             
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
            print(arr)
        gap //= 2
        
 
# Driver code to test above
arr = [12,34,56,23,78,90,77,2,10]
 
n = len(arr)
print ("Array before sorting:")
for i in range(n):
    print(arr[i]),
 
shellSort(arr)
 
print ("\nArray after sorting:")
for i in range(n):
    print(arr[i])
