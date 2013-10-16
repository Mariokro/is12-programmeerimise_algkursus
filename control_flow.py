#!/usr/bin/env python
# -*- coding: utf8 -*- 
#!/usr/bin/python

opilane = "aa"

if opilane == "Mariin":
	print( "Tere!" )
	
elif opilane == "Ardo":
	print ("Ardo-Ardo....")
else:
	print ("Tere! Tundmatu ärandaja.")

print"----------------------------------------------------------"

x = 0
while x<10:
	print "x=" +str(x)
	x = x + 1
print "valmis. x=" +str(x)

print"----------------------------------------------------------"

massiiv = ["Aadu","Beedu","Ceedu","Deedu","Eedu","Feedu","Geedu"]
for element in massiiv:
	if element == "Beedu":
		continue
	print element
	if element == "Feedu":	
		break
print "valmis"
