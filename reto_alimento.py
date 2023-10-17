https://replit.com/@a00574073/Evaluacion-de-Alimentos?v=1

grasa = int(input("¿Cuánta grasa contiene el alimento que vas a consumir? "))
if grasa < 5:
  print("El alimento es sano")
elif grasa < 20:
  print("El alimento es parcialmente sano ")
elif grasa < 30:
  print("El alimento es grasoso")
else:
  print("El alimento es peligroso")  

azucar = int(input("¿Cuánta azúcar tiene el alimento que vas a consumir ?  "))
if azucar < 10:
  print("El alimento es sano")
elif grasa > 10:
  print("El alimento es parcialmente sano ")
elif grasa > 15:
  print("El alimento es muy dulce")
else:
  print("El alimento es peligroso")
  
sodio = int(input("¿Cuánto sodio contiene el aliento que vas a consumir  "))
if sodio < 100:
  print("El alimento es bajo en sodio")
elif sodio > 100:
  print("Cuidado! Alimento peligroso")
else:
  print("No te entendí")
