# Linear search in array
def search(l):
    x = int(input("Enter the integer value you want to find : "))
    Found = False
    for i in range(len(l)):
        if l[i] == x:
            print(f"{x} found at {i} position")
            Found = True
            break
    if not Found:
        print("you entered value not present in the list")
# Driver code
l = [10,20,30,40,50,60,70,80,90,100]
search(l)