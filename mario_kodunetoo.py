# -*- coding: cp1257 -*-
#################################YLESANNE1########################################

tekst=raw_input("Sisesta tekst:")
if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "V2iket2hed ja numbrid"
elif tekst == str(tekst.lower()):
	print "V2iket2hed ja numbriteta"
elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Suurt2hed ja numbrid" 
elif tekst == str(tekst.upper()):
	print "Suurt2hed ja numbriteta"
elif any(c.isdigit() for c in tekst):
	print "Suured v6i v2ikesed tähed ja numbrid"
else:
	print "Suured v6i v2ikesed t2hed ja numbriteta"

print


#################################YLESANNE2########################################

arv1 = int(input("Arv1:"))
arv2 = input("Arv2:")
if arv2<arv1:
	print "Arv2 peab olema v2iksem arv1-st"
kolmega=0;
for X in range(arv1, arv2+1):
	if(X % 3 == 0):
		kolmega = kolmega+1;
		
print kolmega
