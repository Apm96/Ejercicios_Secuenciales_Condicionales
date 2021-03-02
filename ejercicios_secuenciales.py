# 1 Tres personas deciden invertir su dinero para fundar una empresa.
#   Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
#   que cada quien invierte con respecto a la cantidad total invertida.


cantidad1 = float(input("Digite la cantidad de dinero de la primera persona "))
cantidad2 = float(input("Digite la cantidad de dinero de la segunda persona "))
cantidad3 = float(input("Digite la cantidad de dinero de la tercera persona "))

cantidadTotal = cantidad1 + cantidad2 + cantidad3
porc1 = round(cantidad1 / cantidadTotal * 100, 2)
porc2 = round(cantidad2 / cantidadTotal * 100, 2)
porc3 = round(cantidad3 / cantidadTotal * 100, 2)

print(f"El porcentaje de la primera persona con respecto a la cantidad total invertida es {porc1}% \n" +
      f"El porcentaje de la segunda persona con respecto a la cantidad total invertida es {porc2}% \n" +
      f"El porcentaje de la tercera persona con respecto a la cantidad total invertida es {porc3}% \n")


# 2 Una empresa paga a sus empleados además del sueldo base una
#   bonificación especial de $80.000 por cada hijo. Realice un programa
#   en Java que determine el monto de la bonificación y el monto total a
#   pagar al trabajador.

sueldoBase = float(input("Digite el sueldo base del empleado "))
cantHijos = int(input("Digite la cantidad de hijos que tiene el empleado "))
bonificacion = round(cantHijos * 80000, 2)
total = sueldoBase + bonificacion
print(f"El monto de la bonificacion del empleado es {bonificacion} \n" +
      f"El monto total a pagar a el empleado es {total}")

# 3 Un banco da a sus ahorradores un interes de 1.5% sobre el monto
#   ahorrado. Teniendo como dato de entrada el saldo inicial del
#   ahorrador determine el saldo final.

monto = float(input("Digite el monto ahorrado "))
saldoFinal = round((0.15 * monto) + monto, 2)
print(f"El saldo final del ahorrador es {saldoFinal}")


# 4 Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
#   cliente debe dar una cuota inicial del 35% y el resto lo paga en 12
#   cuotas. Determine el valor a pagar por cuota inicial y el monto de
#   cada cuota.

mcuadrado = float(input("Digite la cantidad de metros cuadrado "))
cuotaInicial = round(80000 * mcuadrado * 0.35, 2)
valorcuota = round((80000 * mcuadrado - cuotaInicial) / 12, 2)
print(f"El valor de cuota inicial a pagar es ${cuotaInicial:,} \n" +
      f"El monto de las cuotas es ${valorcuota:,}")

# 5 Una empresa le hace los siguientes descuentos sobre el sueldo base
#   a sus trabajadores: 1% por ley de politica pública, 4% por seguro
#   social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
#   programa en Java que determine el monto de cada descuento y el
#   monto total a pagar al trabajador.

sueldoBase = float(input("Digite el sueldo base del trabajador "))
dPolitica = round(sueldoBase * 0.01, 2)
dSeguroSo = round(sueldoBase * 0.04, 2)
dSeguroFor = round(sueldoBase * 0.005, 2)
dCaja = round(sueldoBase * 0.05, 2)
sueldoTotal = sueldoBase - dPolitica - dSeguroSo - dSeguroFor - dCaja
print(f"El valor de descuento por ley de politica pública es ${dPolitica:,} \n" +
      f"El valor de descuento por seguro social es ${dSeguroSo:,} \n" +
      f"El valor de descuento por seguro forzoso es ${dSeguroFor:,} \n" +
      f"El valor de descuento por caja de ahorro es ${dCaja:,} \n" +
      f"El monto total a pagar a el trabajador es ${sueldoTotal:,}")

# 6 El periódico el Informador cobra por un aviso clasificado un monto
#   que depende del número de palabras, tamaño en cetímetros y
#   número de colores. Cada palabra tiene un costo de $20.000, cada
#   centímetro tiene un costo de $15.000 y cada color tiene un costo de
#   $25.000. Realice un algoritmo que determine el monto a pagar por un
#   aviso clasificado.

numPalabras = int(input("Digite el numero de palabras "))
centimetros = float(input("Digite el tamaño en centimetros (cm) "))
colores = int(input("Digite el numero de colores "))
montoTotal = round((numPalabras * 20000) + (centimetros * 15000) + (colores * 25000), 2)
print(f"El monto a pagar por el aviso clasificado es ${montoTotal:,}")

# 7 Una empresa paga a sus empleados un bono por antigüedad que
#   consiste en $100.000 por el primer año laboral y $120.000 por cada
#   año siguiente. Realice un programa en Java que determine el monto
#   del bono a pagar a un trabajador que tiene varios años en la empresa.

anios = int(input("Digite el numero de años de antiguedad del empleado "))
montoTotal = ((anios - (anios - 1)) * 100000) + ((anios - 1) * 120000)
print(f"El monto a pagar para el trabajador es ${montoTotal:,}")

# 8 Una Universidad le paga a sus profesores $20.000 la hora y le hace
#   un descuento del 5% por concepto de caja de ahorro. Determine el
#   monto del descuento y el monto total a pagar al profesor.

horas = float(input("Digite el numero de horas trabajadas por el profesor "))
descuento = (20000 * horas) * 0.05
montoTotal = (20000 * horas) * 0.95
print(f"El descuento por caja de ahorro es ${descuento:,} \n" +
      f"El monto a pagar a el profesor es ${montoTotal:,}")

# 9 Un centro de comunicaciones alquilan tarjetas para realizar llamadas
#   y cobran el monto consumido de la tarjeta mas un recargo del 20%.
#   Teniendo como dato de entrada el monto inicial y el monto final de la
#   tarjeta, determine el costo de la llamada.

montoInicial = float(input("Digite el monto inicial "))
montoFinal = float(input("Digite el monto final "))
costoLlamada = (montoInicial - montoFinal) + (((montoInicial - montoFinal) * 0.2))
print(f"El costo de la llamada es ${costoLlamada:,}")

# 10 En una fototienda cobran por el revelado de un rollo $1.500 por cada
#    foto. Realice un programa en Java que determine el monto a pagar
#    por un revelado completo sabiendo que adiconalmente le cobran el
#    IVA (16%).

numFotos = int(input("Digite el numero de fotos "))
montoTotal = (1500 * numFotos) + (1500 * numFotos * 0.16)
print(f"El monto a pagar por el revelado completo es ${montoTotal:,}")

# 11 En un hospital existen tres áreas: Ginecología, Pediatría y
#    Traumatología. El presupuesto anual del hospital se reparte
#    conforme a la siguiente tabla:
#    Area - Porcentaje Presupuestal
#    Ginecología - 40%
#    Traumatología - 30%
#    Pediatría - 30%
#    Obtener la cantidad de dinero que recibirá cada área, para cualquier
#    monto presupuestal.

monto = int(input("Digite el monto presupuestal anual "))
montoGine = (monto * 0.4)
montoTrau = (monto * 0.3)
montoPedi = (monto * 0.3)
print(f"La cantidad de dinero que recibirá el área de Ginecología es ${montoGine:,}\n" + 
      f"La cantidad de dinero que recibirá el área de Traumatología es ${montoTrau:,}\n" + 
      f"La cantidad de dinero que recibirá el área de Pediatría es ${montoPedi:,}")

# 12 Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
#    que consiste en dejar gratis el alquiler de una película. Realice un
#    programa en Java que teniendo como dato de entrada el total de
#    películas alquiladas, y el número de días de alquiler, determine el
#    monto a pagar.

numPeliculas = int(input("Digite el de peliculas a alquilar "))
numDias = int(input("Digite el No de dias "))
montoTotal = (numPeliculas - 1) * 1500 * numDias;
print(f"El monto a pagar es ${montoTotal:,}")

# 13 Una Agencia de viajes cobra por un Tour a Cartagena $25.000
#    diarios por persona. Realice un programa en Java que determine el
#    monto a pagar por una familia que desee realizar dicho Tour
#    sabiendo que también cobran el 12% de IVA.

numPersona = int(input("Digite el numero de personas que conforman la familia "))
montoTotal = (numPersona * 25000) + (numPersona * 25000 * 0.12);
print(f"El monto a pagar por la familia es ${montoTotal:,}")

# 14 Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
#    clientes. Cobra por una habitación $100.000 el primer día y por el
#    resto $200.000 por día. Realice un programa en Java que determine
#    el valor total a pagar por la habitación si la estadía fue de varios
#    días.

numDias = int(input("Digite el No de dias de estadia del cliente "))
montoTotal = ((numDias - (numDias - 1)) * 100000) + ((numDias - 1) * 200000);
print(f"El valor total de la habitacion por la estadia de {numDias} dia(s) es ${montoTotal:,}")


# 15 El banco del Pueblo da microcréditos a empresarios para ser
#    cancelados en un lapso de 2 años (24 meses). Al monto del 
#    préstamo se le cobra un interés del 24%. El empresario debe pagar
#    la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
#    cuotas ordinarias. Realice un algoritmo que teniendo como dato de
#    entrada el monto del préstamo, determine el monto total a pagar por
#    el préstamo, el monto de las cuotas especiales y el monto de las
#    cuotas ordinarias.

monto = float(input("Digite el monto del prestamo "))
nuevoMonto = (monto * 0.24) + monto
valorCuotasEspe = (nuevoMonto / 2) / 4
valorCuotasOrdi = (nuevoMonto / 2) / 20


print(f"El valor total a pagar por el prestamo es ${nuevoMonto:,} \n" + 
      f"El monto de las cuotas especiales es ${valorCuotasEspe:,} \n" + 
      f"El valor de las cuotas ordinarias es ${valorCuotasOrdi:,}")





















