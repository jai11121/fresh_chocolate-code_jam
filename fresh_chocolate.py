import random
p=int(input())
c=0
print('enter list')
l=[int(i) for i in input().split()]
for i in range(len(l)):
    if l[i]%p==0:
        c+=1
        l[i]=0
s=[i for i in l if i>0]
print(s)
for i in range(100):
    if len(s)>1:

        m = random.sample(s, 2)
        if (m[0] + m[1]) % p == 0:
            s.remove(m[0])
            s.remove(m[1])
            c += 1
print(s)
for i in range(100):
    if len(s)>2:

        m = random.sample(s, 3)
        if (m[0] + m[1]+m[2]) % p == 0:
            s.remove(m[0])
            s.remove(m[1])
            s.remove(m[2])
            c += 1
print(s)
for i in range(100):
    if len(s)>3:

        m = random.sample(s, 4)
        if (m[0] + m[1]+m[2]+m[3]) % p == 0:
            s.remove(m[0])
            s.remove(m[1])
            s.remove(m[2])
            s.remove(m[3])
            c += 1
print(s)
if (len(s)==0):
    print(c)
else:
    print(c+1)




