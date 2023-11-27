def countMerge(arr,l,m,r):
    left =arr[l:m+1]
    right = arr[m+1:r+1]
    res,i,j,k=0,0,0,l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            res+=(len(left)-i)
        k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
            

        