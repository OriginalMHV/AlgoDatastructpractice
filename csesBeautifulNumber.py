n = int(input())
a = [1,2,4,5]
#Input 3
#Output 2,1,3,5,4


for i in range(1,len(a)):

    if a[i - 1] < n+1 or n-1 < a[i + 1]:
        print(a[i-1] + n + a[i+1])
    elif a[i] > n+1 and n < a[i]:
        print("Solution not found")

