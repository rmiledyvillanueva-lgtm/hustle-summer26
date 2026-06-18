import sys

first_name = input("Nombre:")
print() #blank line

last_name = input("Apellido:")
print() #blank line

print(f"Hi Hi {first_name}!")
print() #blank line

answer = input("Como ha estado tu dia? bien o mal?: ").strip().lower()
if answer == "bien":
    print() #blank line
    print("Me alegra que hayas tenido un excelente dia")
    print() #blank line
    answer3 = input("Te puedo dar un abrazo?").strip().lower()
    print() #blank line
    if answer3 == "si":
        print () #blank line
        print("Te Quiero Mucho <3 *Un fuerte abrazo virtual*")
    elif answer3 == "no":
        print() #blank line
        print(":( ouch")
elif answer == "mal":
    print() #blank line
    hug = input("Lo siento, quieres un abrazo virtual?").strip().lower()
    if hug == "si":
        print() #blank line
        print("Te Amo <3 *abrazos virtuales*")
    elif hug == "no":
        print() #blank line
        print("ah... que triste, pero esta bien, aun asi te quiero")
print() #blank line
print("Oye.. ") #blank line

answer2 = input("Do you know who loves you a lot??").strip().lower()
if answer2 in ("yes", "si"):
    print() # blank line
    quien = input("Quien?")
    print() # blank line
    print(f"hehe si es verdad {quien} te quiere mucho Muchisimo<3")
elif answer2 == "no":
    print() # blank line
    print("Quieres que te recurde quien te ama? Ah..")
    print( "Haha.. Ni modos, ahora vaz a tener que leer un mensaje de alguien que te ama Muchisimo<3" )
print() # blank line
print("Te tengo un mensajito solo para ti")
answer4 = input("Queires leerlo?").strip().lower()
if answer4 == "no":
    print() # blank line
    print("morí xp")
    sys.exit()
elif answer4 == "si":
    print() # blank line
    answer5 = input("enserio si quieres?! ").strip().lower()
    if answer5 == "si":
        print() # blank line
        import webbrowser
        webbrowser.open ("https://docs.google.com/document/d/15K2CziXYAbmrTB3xSnfkRlKEBo0XgX4YCcsTvMXa0cs/edit?usp=sharing")
    elif answer5 == "no":
        pass