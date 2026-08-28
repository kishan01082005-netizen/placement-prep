s="listen"
t="silent"
dict1={}
if len(s)!=len(t):
    print("Not Anagrams")
for k in s:
    if k in dict1:
        dict1[k]+=1
    else:
        dict1[k]=1
for p in t:
    if p in dict1:
        dict1[p]-=1
if all(value == 0 for value in dict1.values()):
    print("Anagrams")
else:
    print("Not Anagrams")