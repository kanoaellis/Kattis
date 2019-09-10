def GCD(g, s):
    if (s == 0):
        return g
    return GCD(s, g % s)

def LCM(x, y):
    return (x * y) // GCD(x, y)

i = 0
a = int(input())
while(i < a):
    b = int(input())
    z = [int(w) for w in input().split()]
    if(b == 1):
        t = z[0]
    elif(b == 2):
        t = LCM(z[0], z[1])
    elif(b == 3):
        t = LCM(z[0], z[1])
        t = LCM(z[2], t)
    elif(b == 4):
        t = LCM(z[0], z[1])
        t = LCM(z[2], t)
        t = LCM(z[3], t)
    elif(b == 5):
        t = LCM(z[0], z[1])
        t = LCM(z[2], t)
        t = LCM(z[3], t)
        t = LCM(z[4], t)
    else:
        break
    if(t > 1000000000):
        print('More than a billion.')
    else:
        print(t)
    i += 1
