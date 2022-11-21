mat = []
for i in range(256):
    mat.append(list(map(int, input().split())))

row1, row2, col1, col2 = 0, 0, 0, 0
for i in range(256):
    flag = True
    for j in range(256):
        if mat[i][j] == 0:
            row1 = i
            flag = False
            break
    if not flag:
        break

    flag = True

for i in range(256):
    flag = True
    for j in range(256):
        if mat[j][i] == 0:
            col1 = i
            flag = False
            break
    if not flag:
        break

for i in range(255, row1, -1):
    flag = True
    for j in range(256):
        if mat[i][j] == 0:
            row2 = i
            flag = False
            break
    if not flag:
        break

    flag = True

for i in range(255, col1, -1):
    flag = True
    for j in range(256):
        if mat[j][i] == 0:
            col2 = i
            flag = False
            break
    if not flag:
        break
    
print((row1, col1), (row1, col2), (row2, col1), (row2, col2))