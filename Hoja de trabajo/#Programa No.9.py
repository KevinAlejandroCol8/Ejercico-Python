#Programa No.9

invers = float(input("Ingrese el monto que va invertir : "))
anio = int(input("Ingrese por cuantos años va invertir : "))

if invers <= 5000:
    porce = 1
    calc = ((invers * porce)/100)
    print("Su interés por año es: " , calc)
    print("La inversion de: Q.", invers, "quedan ganacias de Q." , (calc * anio), "durante  ", anio, " años")

if invers > 5000:
    porce = 2.5
    calc = ((invers * porce)/100)
    print("Su interés por año es: " , calc)
    print("La inversion de: Q.", invers, "quedan ganacias de Q." , (calc * anio), "durante  ", anio, " años")