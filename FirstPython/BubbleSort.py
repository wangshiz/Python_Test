from random import randint

list = []

for i in range(10):
    s = randint(1, 101)
    list.append(s)

print(list)

for i in range(0, len(list)-1):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)
