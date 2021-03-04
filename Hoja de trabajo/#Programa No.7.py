#Programa No.7
peso = float(input("Ingrese su peso en libras: "))
estatura = float(input("Ingrese su estatura en metros: "))

kg = peso * ( 1 / 2.2046)
print("")
print("Tu altura es de: " , round(estatura, 3), "\n" , 
"Tu peso es: ", peso ," lb" , "\n"
"Tu peso es: ", round(kg, 2), "kg"  , "\n",
 "IMC : ", round((kg/pow(estatura, 2)), 2))