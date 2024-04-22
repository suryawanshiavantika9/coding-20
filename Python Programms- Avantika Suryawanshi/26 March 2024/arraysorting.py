size=int(input("ENTER ARRAY SIZE "))
arr=[]
print("Enter the array elements")
for i in range(size):
    element=int(input())
    arr.append(element)

arr.sort()
half=arr[size//2:]
half.sort(reverse=True)
out=arr[:size//2]+half
print("Sorted first half in ascending order and second half in descending",*out,sep="\n")