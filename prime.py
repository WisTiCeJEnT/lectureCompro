n = int(input())
pls = []
ls = []
ans = 0
for i in range(2,n+1):
    ls.append(i)
while(ls):
    tmp = ls[0]
    pls.append(ls.pop(0))
    for i in ls:
        if(i%tmp==0):
            ls.remove(i)
print(pls)
