# 1 Hacer un algoritmo que calcule el total a pagar por la compra de
#   camisas. Si se compran tres camisas o mas se aplica un descuento
#   del 30% sobre el total de la compra y si son menos de tres camisas
#   un descuento del 10%.


valorCamisas = int(input("Digite el valor de las camisetas a comprar "))
numCamisas = int(input("Digite numero de camisetas a comprar "))

montototal = 0

if (numCamisas >= 3):
    montototal = (valorCamisas * numCamisas) * 0.7    
else:
    montototal = (valorCamisas * numCamisas) * 0.9    

print(f"El total a pagar por la compra de las camisas es ${montototal:,}")


# 2 En un supermercado se hace una promoción, mediante la cual el
#   cliente obtiene un descuento dependiendo de un número que se
#   escoge al azar. Si el número escogido es menor que 74 el descuento
#   es del 15% sobre el total de la compra, si es mayor o igual a 74 el
#   descuento es del 20%. Obtener cuanto dinero se le descuenta


numero = int(input("Digite el numero escogido al azar "))
valorCompra = int(input("Digite el valor de la compra "))

montototal = 0
descuento = 0

if (numero < 74):
    montototal = valorCompra * 0.85    
    descuento = valorCompra * 0.15
else:
    montototal = valorCompra * 0.8
    descuento = valorCompra * 0.2

print(f"El total a pagar por la compra es ${montototal:,} \n" + 
      f"El valor descontado es ${descuento:,}")


# 3 Una compañía de seguros está abriendo un departamento de
#   finanzas y estableció un programa para captar clientes, que conssite
#   en lo siguiente: Si el monto por el que se efectúa la fianza es menor
#   que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
#   es mayor que $50.000 la cuota a pagar será el 2% del monto. La
#   afianzadora desea determinar cual será la cuota que debe pagar al
#   cliente.


finanza = int(input("Digite el monto de la finanza "))
cuota = 0

if (finanza < 50000):   
    cuota = finanza * 0.03
else:
    cuota = finanza * 0.02

print(f"El total valor de la cuota que debe pagar el cliente es ${cuota:,}")

# 4 Una fábrica ha sido sometida a un programa de control de
#   contaminación para lo cual se efectúa una revisión de los puntos de
#   contaminación generados por la fábrica. El programa de control de
#   contaminación consiste en medir los puntos que emite la fábrica en
#   cinco días de una semana y si el promedio es superior a los 170
#   puntos entonces tendrá la sanción de parar su producción por una
#   semana y una multa del 50% de las ganancias diarias cuando no se
#   detiene la producción. Si el promedio obtenido de puntos es de 170 o
#   menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
#   desea saber cuanto dinero perderá después de ser sometido a la
#   revisión


p1 = int(input("Digite los puntos del dia 1 "))
p2 = int(input("Digite los puntos del dia 2 "))
p3 = int(input("Digite los puntos del dia 3 "))
p4 = int(input("Digite los puntos del dia 4 "))
p5 = int(input("Digite los puntos del dia 5 "))

valorTotalSemana = int(input("Digite el valor de las ganancias de la semana "))
promedio = (p1 + p2 + p3 + p4 + p5) / 5
perdida = 0

if (promedio > 170):   
    perdida = valorTotalSemana * 0.5    

print(f"El valor que descontara tras la revision es ${perdida:,}")

# 5 Una persona se encuentra con un problema de comprar un automóvil
#   o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
#   mientras el automóvil se devalúa, con el terreno sucede lo contrario.
#   Esta persona comprará el automóvil si al cabo de tres años la
#   devaluación de este no es mayor que la mitad del incremento del
#   valor del terreno. Ayúdale a esta pesona a determinar si debe o no
#   comprar el automóvil.


valor = int(input("Digite el valor del terreno y el auto "))
PorceAuto = float(input("Digite el porcentaje de devaluacion del auto "))
PorceTerreno = float(input("Digite el porcentaje de valorizacion del terreno "))
ValorAutoDevaluado = (valor * (PorceAuto / 100) * 3)
ValorTerrenoAvaluado = (valor * (PorceTerreno / 100) * 3)


if (ValorAutoDevaluado <= (ValorTerrenoAvaluado / 2)):
    print(f"Si comprara el auto porque el valor de la devaluacion del auto: ${ValorAutoDevaluado:,} \n" +
          f"es menor que la mitad del incremento del terreno: ${(ValorTerrenoAvaluado / 2):,}")
else:
    print(f"No comprara el auto porque el valor de la devaluacion del auto: ${ValorAutoDevaluado:,} \n" +
          f"es mayor que la mitad del incremento del terreno: ${(ValorTerrenoAvaluado / 2):,}")
    
# 6 En una fábrica de computadoras se planea ofrecer a los clientes un
#   descuento que dependerá del número de computadoreas que
#   compre. Si las computadoras son menos de cinco se les dará un 10%
#   de descuento sobre el total de la compra; si el número de
#   computadoras es mayor o igual a cinco pero menos de diez se le
#   otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
#   precio de cada computadora es de $11.000.


numcomputadora = int(input("Digite el numero de computadoras a comprar "))
descuento = 0

if (numcomputadora < 5):
    descuento = numcomputadora * 11000 * 0.1
    print(f"El valor del descuento es ${descuento:,}")
elif (numcomputadora >= 5 and numcomputadora < 10):
    descuento = numcomputadora * 11000 * 0.2
    print(f"El valor del descuento es ${descuento:,}")
else:
    descuento = numcomputadora * 11000 * 0.4
    print(f"El valor del descuento es ${descuento:,}")
    
    
# 7 Un proveedor de estéreos ofrece un descuento del 10% sobre el
#   precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
#   independientemente de esto, ofrece un 5% de descuento si la marca
#   es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
#   cualquiera por la compra de su aparato. IVA es del 16%


valorAparato = float(input("Digite el valor del aparato "))
marca = input("Digite el nombre de la marca (NOSY, SONY, LG, OTRA) ")
descuento = 0
total = 0

if (valorAparato >= 2000):
    descuento = valorAparato * 0.1

if (marca == "NOSY"):
    total = ((valorAparato - descuento) * 0.95) + (valorAparato * 0.16)
else:
    total = (valorAparato - descuento) + (valorAparato * 0.16)
    
print(f"El valor total a pagar por el cliente es ${total:,}")


# 8 Una empresa quiere hacer una compra de varias piezas de la misma
#   clase a una fábrica de refacciones. La empresa, dependiendo del
#   monto total de la compra, decidirá que hacer para pagar al fabricante.
#   Si el monto total de la compra excede de $500.000 la empresa tendrá
#   la capacidad de invertir de su propio dinero un 55% del monto de la
#   compra, pedir prestado al banco un 30% y el resto lo pagará
#   solicitando un crédito al fabricante. Si el monto total de la compra no
#   excede de $500.00 la empresa tendrá capacidad de invertir de su
#   propio dinero un 70% y el restante 30% lo pagará solicitando crédito
#   al fabricante. El fabricante cobra por concepto de interes un 20%
#   sobre la cantidad que se le pague a crédito. Obtener la cantidad a
#   inverir, valor del préstamo, valor del crédito y los intereses.


valorCompra = float(input("Digite el valor de la compra "))
cantidadInvertir = 0
prestamo = 0
credito = 0
intereses = 0

if (valorCompra > 500000):
    cantidadInvertir = (valorCompra * 0.55)
    prestamo = (valorCompra * 0.3)
    credito = (valorCompra * 0.15)
    intereses = (credito * 0.2) + credito
else:
    cantidadInvertir = (valorCompra * 0.7)
    credito = (valorCompra * 0.3)
    intereses = (credito * 0.2) + credito
    
print(f"La cantidad a invertir es ${cantidadInvertir:,} \n" +
      f"El valor del prestamo es ${prestamo:,}\n"
      f"El valor del credito es ${credito:,}\n"
      f"El valor de los intereses es ${intereses:,}")

# 9 Leer 2 números; si son iguales que lo multiplique, si el primero es
#   mayor que el segundo que los reste y sino que los sume.


num1 = float(input("Digite el 1 numero "))
num2 = float(input("Digite el 2 numero "))
resultado = 0

if (num1 == num2):
    resultado = num1 * num2
elif (num1 > num2):    
    resultado = num1 - num2
else:
    resultado = num1 + num2
    
print(f"El resultado de la operacion es {resultado:,}")

# 10 Leer tres números diferentes e imprimir el número mayor de los
#    tres


num1 = float(input("Digite el 1 numero "))
num2 = float(input("Digite el 2 numero "))
num3 = float(input("Digite el 3 numero "))

if ((num1 == num2 or num1 == num3) or (num2 == num3 or num2 == num1)):
    print("Los numeros deben ser diferentes")
elif (num1 > num2 and num1 > num3):    
     print(f"El numero {num1:,} es el mayor")
elif (num2 > num1 and num2 > num3):    
     print(f"El numero {num2:,} es el mayor")
elif (num3 > num2 and num3 > num1):    
     print(f"El numero {num3:,} es el mayor")
    
    
    



















    