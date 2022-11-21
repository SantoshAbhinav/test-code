inp = int(input())

def base3(inp):
    s3 = ''
    while inp != 0:
        r = inp%3
        inp = inp//3
        s3 += str(r)
    return s3[::-1]

print(base3(inp))