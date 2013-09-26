from random import randint
klass=["Arti","Art","Janis","Kerto","Eveli","Jasper","Mario","Kairo","Ardo","Janar","Katerin","Rait","Aulis","Mariin","Timo"]
n=1
while n<=100:
    print (klass)
    c = len(klass)-1
    a = randint(0,c)
    b = klass[a]
    print(b)
    del klass[a]
    print (sorted(klass))
    klass = ((sorted(klass) + [b]))
    n=n+1







