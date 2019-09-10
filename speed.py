a = int(input())
while(a != -1):
    i, m, y, z = 0, 0, 0, 0
    aa, bb, = 0, 0
    while(i < a):
        x = [int(w) for w in input().split()]
        y = x[0]
        z = x[1] - bb
        bb = x[1]
        m = y * z + m
        i += 1
    print(m, ' miles')
    a = int(input())
