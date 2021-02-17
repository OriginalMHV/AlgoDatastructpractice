#String A, C, G, and T.
#Find the max time String repeat
#input(string)

n = list(input())
count = 0
maxAmount = 0


for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count += 1
        if maxAmount <= count:
            maxAmount = count
    elif n[i] != n[i+1]:
        count = 0


print(maxAmount+1)





