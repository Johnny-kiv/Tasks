n = int(input("Enter the number n: "))
arr = []
for i in range(1,n):
    if i%2==1:
        arr.append(i)
for i in arr:
    print(i,end=" ")