# create the initial variables below
age = 28 #age of the individual in years
sex = 0 #0 for female, 1 for male*
bmi = 26.2 #individual’s body mass index
num_of_children = 3 #number of children the individual has
smoker = 0 #0 for a non-smoker, 1 for a smoker

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print ('''1. This person's insurance cost is ''', insurance_cost, ' dollars')

# Age Factor
age += 4
print (age)
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print ('''2. This person's new insurance cost is ''', new_insurance_cost, ' dollars')

change_in_insurance_cost = new_insurance_cost - insurance_cost
print ("3. The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

# BMI Factor
age = 28 #reset age
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print ("4. The change in estimated insurance cost after increasing the BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")

# Male vs. Female Factor
bmi = 26.2 #reset bmi
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print ("5. The change in estimated costo for being male instaed of female is " + str(change_in_insurance_cost) + " dollars")

# Extra Practice
sex = 0 #reset sex
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print ("6. The change in estimated costo for being smoker instaed of nonsmoker is " + str(change_in_insurance_cost) + " dollars")

smoker = 0 #reset smoker
num_of_children = 7
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print ("8. The change in estimated costo for have 3 more children is " + str(change_in_insurance_cost) + " dollars")
