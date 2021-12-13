print("hello, wat is jouw naam")

print("hallo, wat is jouw naam")
name = input ("type je naam ")

print("Welkom "+ name )
start = input("wil je een quiz maken " + name + " ") 

if start =="ja":
    print("laten we beginnen! ")

    eerste_vraag = input ("vind je deze opleiding leuk? ")
        
    if eerste_vraag =="ja":
        print("ik vind het ook leuk! ")
    else:
        print("verander dan van opleiding. ")

    tweede_vraag = input ("hou je van cola? ")
        
    if tweede_vraag =="ja":
        print("ik vind ook! ")
    else:
        print("oh jammer ")

    derde_vraag = input ("ben je gelukkig? ")
        
    if derde_vraag =="ja":
        print("ik ook ")
    else:
        print("jammer ")


else:
    print("jammer ")