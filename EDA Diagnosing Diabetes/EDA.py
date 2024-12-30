import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv("diabetes.csv")
print(diabetes_data.head())

#How many columns (features) does the data contain?
print(len(diabetes_data.columns))

#How many rows (observations) does the data contain?
print(len(diabetes_data))

#Do any of the columns in the data contain null (missing) values?
print(diabetes_data.isnull().sum())

#To investigate further, calculate summary statistics on diabetes_data using the .describe() method.
print(diabetes_data.describe())

#Use the following code to replace the instances of 0 with NaN in the five columns mentioned:
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

#Next, check for missing (null) values in all of the columns just like you did in Step 5. Now how many missing values are there?
print(diabetes_data.isnull().sum())

#Print out all of the rows that contain missing (null) values.
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#Next, take a closer look at the data types of each column in diabetes_data.Does the result match what you would expect?
print(diabetes_data.info())

#To figure out why the Outcome column is of type object (string) instead of type int64, print out the unique values in the Outcome column.
print(diabetes_data.Outcome.unique())

#How might you resolve this issue?
#R: A possible next step would be to replace instances of 'O' with 0 and convert the Outcome column to type int64.

#Here are some ways you might extend this project if you’d like:
#1. Use .value_counts() to more fully explore the values in each column.
print(diabetes_data.Pregnancies.value_counts())
print(diabetes_data.Glucose.value_counts())
#2. Investigate other outliers in the data that may be easily overlooked.
#3. Instead of changing the 0 values in the five columns to NaN, try replacing the values with the median or mean of each column.
