left_table = []
right_table = []

file = open("day1/input.txt",'r')

for line in file:
    tab = line.strip().split('   ')
    print(tab)
    left_table.append(tab[0])
    right_table.append(tab[1])

similarity_score = 0

for i in range(len(left_table)):
    counter = 0 
    for j in range(len(right_table)):
        if left_table[i] == right_table[j]:
            counter+=1
    similarity_score += int(left_table[i]) * counter

print(similarity_score) 
