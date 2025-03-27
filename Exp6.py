cet = {"Harshit", "Raj", "Jeevan", "Nitesh"}
jee = {"Harshit", "Tanisq", "Muzammil", "Raj"}
neet = {"Suyash", "Raj", "Harshit", "Nitesh"}

def showunion(a, b, c):
    print("Students appearing for CET, JEE or NEET:")
    print(set.union(a, b, c))

def showintersection(a, b, c):
    print("Students present in CET, JEE and NEET:")
    print(set.intersection(a, b, c))

def showdifference(a, b):
    print("Students present in CET but not in JEE:")
    print(set.difference(a, b))

def showdifference_jee_neet(b, c):
    print("Students present in JEE but not in NEET:")
    print(set.difference(b, c))

def showdifference_neet_cet(c, a):
    print("Students present in NEET but not in CET:")
    print(set.difference(c, a))

def showsymmetric_difference(a, b):
    print("Students present in CET or JEE but not both:")
    print(set.symmetric_difference(a, b))

showunion(cet, jee, neet)
showintersection(cet, jee, neet)
showdifference(cet, jee)
showdifference_jee_neet(jee, neet)
showdifference_neet_cet(neet, cet)
showsymmetric_difference(cet, jee)
