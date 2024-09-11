import array
arr = array.array('i', [1, 2, 3, 1, 5])
print("The new created array is : ")
for i in range(0, 5):
    print(arr[i])

print("\r")
print("The popped element is : ")
print(arr.pop(2))
