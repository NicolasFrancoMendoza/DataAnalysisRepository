names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
#Exploring List Data
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs,names))
print(medical_records)

#Selecting List Elements
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records")

first_medical_record = medical_records[0]
print("Here is the fist medical record: " + str(first_medical_record))

#Sorting Lists
medical_records.sort()
print("Here are the medical records sorted by insurance cost " + str(medical_records))

#Slicing Lists
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records " + str(priciest_three))

#Counting Elements in a List
occurrences_paul = names.count("Paul")
print("There are 2 individuals with the name " + str(occurrences_paul) + " in our medical records.")

#Extra
other_medical_records = list(zip(names,insurance_costs))
print(other_medical_records)
other_medical_records.sort()
print("Extra 1: Here are the medical records sorted by name " + str(other_medical_records))

middle_five_records = medical_records[3:8]
print("Extra 2: " + str(middle_five_records))
