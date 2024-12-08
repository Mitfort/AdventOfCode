file = open("day3/input.txt",'r')

result = 0
mul = "mul(x,y)"
numbers = ['0','1','2','3','4','5','6','7','8','9']
enabled = True

for line in file:
    for i in range(len(line)):
        if line[i] == 'd' and line[i + 1] == 'o' and line[i+2] == '(' and line[i + 3 ] == ')':
            enabled = True

        if line[i] == 'd' and line[i + 1] == 'o' and line[i+2] == 'n' and line[i+3] == '\'' and line[i+4] == 't' and line[i+5] == '(' and line[i+6] == ')':
            enabled = False

        if line[i] == 'm' and line[i+1] == 'u' and line[i+2] == 'l' and line[i+3] == '(':
            lineCopy = line
            j = i + 4
            num1 = ""
            while (lineCopy[j] != ','):
                if lineCopy[j] not in numbers:
                    break
                else:
                    num1 += lineCopy[j]
                    j+=1
            num2 = ""
            while(lineCopy[j+1] != ')'):
                if lineCopy[j+1] not in numbers:
                    break
                else:
                    num2 += lineCopy[j+1]
                    j+=1
            if len(num1) <= 3 and len(num1) > 0:
                num1 = int(num1)
            else:
                continue
            if len(num2) <= 3 and len(num2) > 0:
                num2 = int(num2)
            else:
                continue
            
            if lineCopy[j+1] == ')' and enabled:
                result += num1 * num2
print(result)