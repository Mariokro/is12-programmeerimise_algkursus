#!/usr/bin/python
from random import randint
kuulid = ['s']*5 + ['m']*10 + ['v']*15
n=randint(0,len(kuulid))
kuul1=kuulid[n]
del kuulid[n]
print kuul1
kuul2=kuulid[n-1]
print kuul2





	

