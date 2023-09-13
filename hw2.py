list_1 = [5, -1, 6, 9, -5, -3, 10, 6, -7, 8, 9, 11, 0, -8, 10]
list_2 = []
min = 2
max = 8

for i in range(len(list_1)):
     if list_1[i] >= min and list_1[i] <= max:
         list_2.append(i)
print(list_2)