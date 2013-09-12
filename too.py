print "abc".capitalize()
str = "str.center paneb lause nende vahele"
print str.center(41, "*")

print	#
str = "count loendab mitu kysitud t2hte on"
sub = "o"
print "Selles lauses on : ", str.count(sub, 0, 41), "O'd";

print	#
str = "See on lause";
str = str.encode('base64','strict');
print "kodeeritud lause: " + str;
print "lahti-kodeeritud lause: " + str.decode('base64','strict')
print (("v2ikesedt2hedSUURTEKST2HTEDEKS").swapcase())

print	#
abc = ("kes on siin")
print (abc.expandtabs(0))
print (abc.expandtabs(16))
print (str.find("es",1))
print (str.find("ii",1))

print	#endswith
str = "See on n2idis lause";
suffix = "lause";
print str.endswith(suffix);

print 	#
str = "See on n2\tidis lause";
print str.expandtabs(16);

print 	#
print "123".zfill(6)

str = "see on n2idis lause";
print str.zfill(40);

print "0." + "23".zfill(6)

print 	#
str = u"aasta2013";  
print str.isdecimal();

str = u"2013";
print str.isdecimal();

print #

tekst = "Politsei kontrollib\n neljap2eval yle Eesti turvavarustuse kasutamist,\n eelk6ige turvavoo ning laste turvavarustuse kasutamist. "

print tekst

print #

print """
T2na on programmeerimise alused		Aigar ei jaga biiti
Homme on k6rgem_mate			Aivar kytab pliiti
Tuleb veel majanduse tund		LSD kodus magab 66ndsat und
"""
print #





























