#input int and list
#map the list for more inputs
#split() for easy inputs
#find the n(t) -> k[i] moved first

n = int(input())
k = list(map(int, input().split()))
counter = 0
for i in range(1, len(k)):
    if k[i] < k[i-1]:
        counter += (k[i-1] - k[i])
        k[i] = k[i-1]
print(counter)








