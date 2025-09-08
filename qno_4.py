 # 1
 # 1*
 # 1*3
 # 1*3*
 # 1*3*5

rows = 5
num = 1 

for i in range(1, rows + 1):
    line = ""
    for j in range(1, i + 1):
        if j % 2 == 0:
            line += "*"
        else:
            line += str(num)
            num += 2  
print(line)