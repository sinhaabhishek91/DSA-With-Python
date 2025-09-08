#linear search
def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10,22,30,40,30,50,60,30,80,90]
x = int(input("Enter the value you want to search: "))
result = linearsearch(arr,x)
print("Searched item found at index ",result)
