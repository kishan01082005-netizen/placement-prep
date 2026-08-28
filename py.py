s="TREE"
dict={}
for k in s:
    if k in dict:
        dict[k]+=1
    else:
        dict[k]=1
print(sorted(dict.items(),key=lambda x:x[1],reverse=True))