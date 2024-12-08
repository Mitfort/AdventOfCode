left_table = []
right_table = []

file = open("C:/Users/Jerzy/source/python/adventOfCode/day1/input.txt",'r')

for line in file:
    tab = line.split('   ')
    print(tab)
    left_table.append(tab[0])
    right_table.append(tab[1])

right_table.sort()
left_table.sort()

total_dist = 0

for i in range(len(right_table)):
    total_dist += abs(int(right_table[i]) - int(left_table[i]))

print(total_dist)