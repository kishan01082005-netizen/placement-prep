arr=[1,2,2,3,3,4]
hashmap={}
for num in arr:
    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1
print(hashmap)

for j in hashmap:
    if hashmap[j] > 1:
        print(j)