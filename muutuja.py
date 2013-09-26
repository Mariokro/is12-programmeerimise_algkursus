#!/usr/bin/python
from random import randint
klass = ['Aigar', 'Mario', 'Janis', 'Ardo', 'Aulis', 'Chuck Norris', 'Sylvester Stallone', 'Jackie Chan', 'Van Damme']
l=len(klass)-1
print (klass[randint(0,l)])
print ""
print ""
klass= ['a','b','c','d']
print klass
n=2
element=klass[n]
del klass [n]
klass=klass+[element]
print klass


