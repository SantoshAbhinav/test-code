inp = int(input())

LCD_char = {'0', '1', '2', '5', '6', '8', '9'}
lst = [0, 1, 2, 5, 6, 8, 9]

if inp < 7:
    print(lst[inp])
else:
    count = 7
    num = 9
    while count <= inp:
        num += 1
        s = str(num)
        flag = True
        for i in s:
            if i not in LCD_char:
                flag = False
                break
        if flag:
            count += 1
            
    print(num)

