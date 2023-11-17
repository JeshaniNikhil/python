l=[10,30,40,50,"hello"]
print(type(l))

print(l[3],l[4])

print(l[0:2])

print(l[0::2])

print(l[3:])

print(l[-1::-2])

print(l[-1::-1])

t=len(l)

for n in range(t):
    print(l[n])
for a in l:
    print(a)
for n in range(t-1,-1,-1):
    print(l[n])
