names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
#Creating a For Loop
total_cost = 0

for sumar in actual_insurance_costs:
  total_cost += sumar

average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost))

#Using Range in Loops
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost))

#Conditions inside a Loop
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  if insurance_cost < average_cost:
    print("The insurance cost for " + name + " is above average.")
  elif insurance_cost > average_cost:
    print("The insurance cost for " + name + " is below average.")
  else:
    print("The insurance cost for " + name + " is equal average.")

#Creating a List Comprehension
updated_estimated_costs = [i*11/10 for i in estimated_insurance_costs]
print(updated_estimated_costs)

#Extra 1. Convertir el primer FOR a WHILE
contador = 0
total_cost = 0
while contador < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[contador]
  contador += 1

average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost))

#Extra 2. Modificar el segundo FOR para que cálcuyla q tan lejos por encima o debajo está el promedio del costo estimado
for i in range(len(names)):
  name = names[i]
  insurance_cost = estimated_insurance_costs[i] - average_cost
  print("The difference between the average the estimated cost insurance is " + str(insurance_cost) + " to " + name)
