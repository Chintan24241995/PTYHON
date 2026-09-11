# import numpy as np

# py -m pip install numpy

# import numpy as np

# salary = np.array([20000, 30000, 40000])

# print(salary*1.10)

# import numpy as np

# 4. Python List vs NumPy Array
# Feature	Python List	NumPy Array
# Speed	Slow	Fast
# Memory	High	Low
# Mathematical Operations	Difficult	Easy
# Data Handling	Flexible	Efficient
# Example 1: Addition

# list1 = [10, 20, 30]
# print(list1 + list1)

# import numpy as np

# arr = np.array([10,20,30])
# print(arr + arr)

# 5. Creating Arrays in NumPy
# 5.1 Creating 1D Array
# marks = np.array([85, 90, 78, 92])
# print(marks)


# Real World Example
# Monthly Sales:
# import numpy as np

# sales = np.array([12000, 15000, 18000, 20000])
# print(sales)

# 5.2 Creating 2D Array

# employee_data = np.array([
#     [101, 25000],
#     [102, 30000],
#     [103, 35000]
# ])
# print(employee_data)

# Creating Array using zeros()



# Lecture 2.0 NUMPY

# 2.1 Using reshape()



# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# new_arr = arr.reshape(2,3)
# print(new_arr)



# Lecture 3
# concatenate()
# import numpy as np
# jan_sales = np.array([10000,15000,20000])
# feb_sales = np.array([25000,30000,35000])

# combined = np.concatenate(
#     (jan_sales, feb_sales)
# )
# print(combined)


# Vertical Stack
# import numpy as np
# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])

# print(np.vstack((arr1,arr2)))


# Horizontal Stack
# import numpy as np
# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])
# print(np.hstack((arr1,arr2)))


# Spiltting Array
# import numpy as np
# sales = np.array([
#     10000,20000,30000,
#     40000,50000,60000
# ])

# print(np.split(sales,2))


# arr = np.arange(12)
# print(np.split(arr,4))


# Broadcasting in NUMPY
# salary = np.array([
#     20000,
#     30000,
#     40000
# ])
# print(salary + 5000)
# print(salary * 1.10)

# Broadcasting with 2D Arrays

# sales = np.array([
#     [1000,2000],
#     [3000,4000]
# ])

# print(sales + 100)


# Loading CSV Files in NumPy

# file = np.genfromtxt(
#     'employee.csv',
#     delimiter=',',
#     dtype=str,
#     skip_header=1
# )

# print(file)








# Pandas Lecture 1

# pip install pandas

import pandas as pd

df = pd.read_csv("sales.csv")











