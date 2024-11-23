# Add your code here
#Storing patient names and insurance costs
#1
medical_cost = {}
#2
medical_cost["Marian"] = 6607.0
medical_cost["Vinay"] = 3225.0
#3
medical_cost.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
#4
#print(medical_cost)
#5
medical_cost["Vinay"] = 3325.0
#print(medical_cost)
#6
total_cost = 0
#7
average_cost = total_cost/len(medical_cost)
#print("Average Insurance Cost: " + str(average_cost))
#List Comprehension to Dictionary
#8
names = ["Marina","Vinay","Connie","Isaac","Valentina"]
ages = [27,24,43,35,52]
#9
zipped_ages = zip(names,ages)
#10
names_to_ages = {key:value for key, value in zipped_ages}
#print(names_to_ages)
#11
marina_age1 = names_to_ages.get("Marina",0)
#print("Marina's age is {marina_age}".format(marina_age=marina_age1))
#Using a Dictionary to create a medical database
#12
medical_records = {}
#13
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
#14
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
#15
#print(medical_records)
#16
#print(medical_records["Connie"])
#17
medical_records.pop("Vinay")
#18
for patient in medical_records:
  age = medical_records[patient]["Age"]
  sex = medical_records[patient]["Sex"]
  bmi = medical_records[patient]["BMI"]
  children = medical_records[patient]["Children"]
  smoker = medical_records[patient]["Smoker"]
  costs = medical_records[patient]["Insurance_cost"]
  print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(Name=patient,Age=age,Sex=sex,Smoker=smoker,BMI=bmi,Insurance_cost=costs))
#19 Extra
def update_medical_records(name, cost):
  medical_cost[name] = cost
  print(medical_cost)

update_medical_records("El pepe", 1000)