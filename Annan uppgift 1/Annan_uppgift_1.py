a = int(input("Hur manga poang fick du?"))
if a<=100 and a>=88:
    print("Grattis du fick ett A :)!")
elif a<88 and a>= 76:
    print("Grattis du fick ett B!")
elif a<76 and a>= 64:
    print("Grattis du fick ett C.")
elif a<64 and a>= 52:
    print("Du fick ett D.")
elif a<52 and a>= 40:
    print("Du fick ett E, plugga mer nasta gang!")
elif a<40 and a>=0:
    print("Du fick ett F, jag ar besviken pa dig!")
else:
    print("HAHAHAH hur kan du fa mer an 100 poang, javla fuskare.")
