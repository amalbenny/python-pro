print("Which one you need\n kg to pound (1),\n pound to kg(2)\n Kilogram to Gram\n \"Type the associated number to required function\"")
math= input()
if (math=="1"): #kg to pound
    print(" Kilogram to Pound calc") #multiply the mass value by 2.205
    kg_p = float(input(" Kilogram:"))
    p_frkg= kg_p*2.205
    print("\n In pound :")
    print(p_frkg)
if(math=="2"):
    print(" Pound to kg clac")
    p_kg = float(input(" Pound:"))
    kg_frp=p_kg/2.205
    print("\n in kg")
    print(kg_frp)
if(math=="3"):
    kg_g = float(input(" Kilogram: "))
    g_frkg=kg_g*1000
    print("\n In kg: ")
    print(g_frkg)
