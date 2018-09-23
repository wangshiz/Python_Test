import random

list = []

for i in range(10):
    s = random.randint(1, 101)
    list.append(s)

print(list)

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)

