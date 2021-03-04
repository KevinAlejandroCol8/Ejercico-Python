#Programa No.10

op1 = input("Ha comprado barreno (si/no) ")

if op1 == "si":
    barreno = int(input("Cuantos barrenos ha comprado: "))
else:
    barreno = 0   

op2 = input("Ha comprado sierra (si/no) ")

if op2 == "si":
    sierra = int(input("Cuantas sierra ha comprado: "))
else:
    sierra = 0

pesobarre = barreno * 112
pesosierra = sierra * 75
suma = pesobarre + pesosierra
print()
print("Cantidad de barrenos", barreno , "con un peso de ", pesobarre, "kg")
print("Cantidad de sierra", sierra , "con un peso de ", pesosierra, "kg")
print("Peso del paquete total es de: ", suma)