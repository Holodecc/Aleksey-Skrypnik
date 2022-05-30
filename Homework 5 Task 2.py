import random
s1 = []
s2 = []
s3 = []
a1 = random.randint(1,10)
b1 = random.randint(1,10)
c1 = random.randint(1,10)
d1 = random.randint(1,10)
e1 = random.randint(1,10)
f1 = random.randint(1,10)
g1 = random.randint(1,10)
h1 = random.randint(1,10) 
i1 = random.randint(1,10)
j1 = random.randint(1,10)
a2 = random.randint(1,10)
b2 = random.randint(1,10)
c2 = random.randint(1,10)
d2 = random.randint(1,10)
e2 = random.randint(1,10)
f2 = random.randint(1,10)
g2 = random.randint(1,10)
h2 = random.randint(1,10) 
i2 = random.randint(1,10)
j2 = random.randint(1,10)
string1 = 0
string2 = 0
string3 = 0
while string1 !=1:
    s1.append(a1)
    s1.append(b1)
    s1.append(c1)
    s1.append(d1)
    s1.append(e1)
    s1.append(f1)
    s1.append(g1)
    s1.append(h1)
    s1.append(i1)
    s1.append(j1)
    print(s1)
    string1 = string1 + 1
while string2 !=1:
    s2.append(a2)
    s2.append(b2)
    s2.append(c2)
    s2.append(d2)
    s2.append(e2)
    s2.append(f2)
    s2.append(g2)
    s2.append(h2)
    s2.append(i2)
    s2.append(j2)
    print(s2)
    string2 = string2 + 1
for i in s1:
    if i in s2:
        s3.append(i)
print(s3)



    
