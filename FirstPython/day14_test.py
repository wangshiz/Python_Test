lst = ["123","1234","12345"]
lst1 = [i for i in lst if len(i) > 3]
print(lst1)

print([(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y%2==1])

lst = [3, 6, 9]
M = [[i-2, i-1, i - 0] for i in lst]
print(M)
lst2 = [i[2] for i in M]
print(lst2)

lst3 = [(str(lst2[i]) + str(i)) for i in range(len(lst2))]
print(lst3)