s1 = input()
s2 = input()

last_char = s2[-1]
count = 0
for i in s1:
    if i == last_char:
        count += 1
        
print(count)