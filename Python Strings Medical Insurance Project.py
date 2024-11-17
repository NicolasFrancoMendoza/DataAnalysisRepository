medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#Working with Strings
#1. print
#print (medical_data)

#2
updated_medical_data = medical_data.replace("#","$")
#print (updated_medical_data)

#3
num_records = 0

#4
for i in updated_medical_data:
  if i == "$":
    num_records += 1

#5
#print("There are " + str(num_records) + " medical records in the data.")

#Splitting Strings
#6
medical_data_split = updated_medical_data.split(";")
#print(medical_data_split)

#7
medical_records = []

#8
for i in medical_data_split:
  medical_records.append(i.split(","))

#print(medical_records)

#Cleaning Data
#9
medical_records_clean = []

#10/11/12
for record in medical_records:
  record_clean = []
  for i in record:
    record_clean.append(i.strip())
  medical_records_clean.append(record_clean)

#13
#print(medical_records_clean)

#Analyzing Data
#14/15
for record in medical_records_clean:
  #print(record[0]) #14
  #print(record[0].upper()) #15
  ele = 0

#16
names = []
ages = []
bmis = []
insurance_costs = []

#17
for i in medical_records_clean:
  contador = 0
  for j in i:
    if contador == 0:
      names.append(j)
      contador += 1
    elif contador == 1:
      ages.append(j)
      contador += 1
    elif contador == 2:
      bmis.append(j)
      contador += 1
    else:
      insurance_costs.append(j)
      contador = 0

#18
print(names)
print(ages)
print(bmis)
print(insurance_costs)

#19
total_bmi = 0

#20
for i in bmis:
  total_bmi += float(i)

#21
average_bmi = total_bmi/len(bmis)
#print("Average BMI: " + str(average_bmi))

#Extra
#22.1 Calculate the average insurance cost in insurance_costs
total_insurance_costs = 0

for i in insurance_costs:
  cost_fixed = i.replace("$","")
  total_insurance_costs += float(cost_fixed)

average_cost = total_insurance_costs/len(insurance_costs)

print("Average Costs: $" + str(average_cost))

#22.2 Write a for loop that outputs a string for each individual
for i in range(0,len(names)):
  print("{name} is {age} years old with a BMI of {bmi} and an insurance cost of {cost}".format(name=names[1],age=ages[i],bmi=bmis[i],cost=insurance_costs[i]))

