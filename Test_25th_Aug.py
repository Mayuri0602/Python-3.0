arr = [1,2,3,2,4,5,1,6,3]
new_arr = []
duplicates = []
for i in arr:
    if i in new_arr and i not in duplicates:
        duplicates.append(i)
    else:
        new_arr.append(i)
print("Duplicate elements: ",duplicates)    



arr = [12,45,1,-1,45,54,23]
new_arr = list(set(arr))
new_arr.sort()
print("Second largest number: ",arr[-2])



for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()



arr = [1, 5, 7, -1, 5]
target = 6
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))
print(pairs)



arr = [0,1,9,8,4,0,0,2,7,0,6,0]
pos = 0  
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print(arr)