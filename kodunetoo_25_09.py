from random import randint
klass=["Arti","Art","Janis","Kerto","Eveli","Jasper","Mario","Kairo","Ardo","Janar","Katerin","Rait","Aulis","Mariin","Timo"]
for i in xrange (100):
    print (klass)
    c = len(klass)-1
    a = randint(0,c)
    b = klass[a]
    print(b)
    del klass[a]
    print (sorted(klass))
    klass = ((sorted(klass) + [b]))
    






