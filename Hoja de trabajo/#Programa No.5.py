#Programa No.5

clse = int(input("Cuantas clases recibe por semana: "))
horas = int(input("Cuantas horas estudias "))
minu = int(input("Cuantas minutos estudias "))

clHora = clse * 30
convrs1 = (clHora/60) 
convrs2 = (minu/60)
suma = (clse+convrs1) + (horas + convrs2)
print()
print("tiempo de clase ", (clse+convrs1), "Horas\n",
"Tiempo en estudio ",(horas + convrs2),"Horas\n",
"Tiempo invertido en la semana ", suma , "Horas")