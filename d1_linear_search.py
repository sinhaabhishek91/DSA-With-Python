# Linear search in array *
# function difinitaion
# time complexity : o(n)
# space complexity : o(1)
def search(l,x):
    for i in range(len(l)):     # it count the lent of list which starts with 0 to n
        if l[i] == x:           # it will check the condition which is equal to x or not
            return i            # if found in the list it will return 1 
    return -1                   # while not foun in the list it will return -1
l = [20,45,27,47,55,67,75,88,90]
x = int(input("Enter the integer value you want to search : "))
result = search(l,x)
print("Searching element is present at ",result)