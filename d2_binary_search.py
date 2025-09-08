# Binary search Algorithm using recurssion
# function difination
def binarysearch(arr,x,i,j):
    while i <= j:
        mid = i+(j-i)//2        # it find the mid index in array
        if arr[mid] == x:       #if x found at mid index it return smae output
            return mid
        elif arr[mid] < x:      #if mid less then x it move to right side in array
            return binarysearch(arr,x,mid+1,j)  #function recursion search x in arr mid+1 to j
        else:
            # if mid greater than x it move to left, search x in arr and start with i to mid-1
            return binarysearch(arr,x,i,mid-1)  
    return -1
#Driver code
arr = [10,20,30,40,50,60,70,80,90]
x = int(input("Enter the number you want to search : "))
i = 0
j = len(arr)-1
result = binarysearch(arr,x,i,j)
print("Searching element found at index no : ",result)