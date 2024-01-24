a = int(input())
c = 0
f = 0
for i in range(a):
    j = 0
    b = input()
    c += 1
    if 'кот' in b.lower():
        for j in range(len(b)):
            if 'к' in b[j]:
                if 'о' in b[j + 1]:
                    if 'т' in b[j + 2]:
                        print(c, j + 1)
                        break