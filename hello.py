print("hello")
sum = 0
for m in range(1,101):
    sum+=m
print("打印和",sum)
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",(i*j),end="\t")
    print()
