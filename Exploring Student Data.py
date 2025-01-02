# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe(include="all"))

# Calculate mean
mean = students.math_grade.mean()
print("Mean: " + str(mean))

# Calculate median
median = students.math_grade.median()
print("Median: " + str(median))

# Calculate mode
mode = students.math_grade.mode()[0]
print("Mode: " + str(mode))

# Calculate range
range_s = students.math_grade.max() - students.math_grade.min()
print("Range: " + str(range_s))

# Calculate standard deviation
std_deviation = students.math_grade.std()
print("STD DEV: " + str(std_deviation))

# Calculate MAD
mad = students.math_grade.mad()
print("MAD: " + str(mad))

# Create a histogram of math grades
sns.histplot(x="math_grade",data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x="math_grade",data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students.Mjob.value_counts())

# Calculate proportion of students with mothers in each job category
print(students.Mjob.value_counts(normalize=True))

# Create bar chart of Mjob
sns.countplot(x="Mjob",data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()
plt.close()

#Now that we’ve walked you through an exploration of math_grade and Mjob in more detail, take some time to explore the rest of the columns in the dataset! Which kinds of summary statistics and visualizations can you use to summarize these columns?
