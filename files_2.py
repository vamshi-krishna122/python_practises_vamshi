# You have an input file called expenses.csv that stores daily expense records in this format:
# 2025-10-01,Food,250
# 2025-10-01,Travel,100
# 2025-10-02,Shopping,400
# 2025-10-02,Food,150
# 2025-10-03,Entertainment,300
# 2025-10-03,Food,200
# 2025-10-04,Travel,250
# Each line represents:
# Date, Category, Amount
# ________________________________________
# Tasks
# Write a Python program that:
# 1.	Reads all records from expenses.csv.
# 2.	Calculates:
# o	Total expense for the month.
# o	Total expense per category.
# o	Day with the highest total expense.
# 3.	Writes a summary report into a new file monthly_summary.txt in the following format:
# ================= Expense Summary (October 2025) =================
# Total Monthly Expense: ₹1650

# Category-wise Breakdown:
# Food          : ₹600
# Travel        : ₹350
# Shopping      : ₹400
# Entertainment : ₹300

# Highest Spending Day: 2025-10-02 (₹550)
# =================================================================


import os
import csv

def read_expenses(filename):
    path = os.getcwd()

    new_path = os.path.join(path,filename)

    try:
        with open(new_path,'r') as file:
            file = open(new_path,'r')
            data  = list(csv.reader(file))
            return data
    except Exception as e:
        print("File is not present in the location")
    
    return ""

def calculat_summary(data):
    dict_1 = {}
    dict_2 = {}
    for i in range(1,len(data)):
        k = int(data[i][2])
        if dict_1.get(data[i][1])==None:
            dict_1[data[i][1]]= k
        else:
            dict_1[data[i][1]] += k
        

        if dict_2.get(data[i][0])==None:
            dict_2[data[i][0]] = k 
        else:
            dict_2[data[i][0]] += k

    total = 0 
    for i in dict_1.values():
        total += i
    
    output_summary = ""
    output_summary += f"Total Month Expenses : {total} \n"
    output_summary += "Category wise Breakdown\n"
    for i in dict_1.keys():
        output_summary += f"{i} : {dict_1[i]} \n"

    high_spent_amount = 0 
    high_spent_date = ""

    for i in dict_2.keys():
        if dict_2[i] > high_spent_amount:
            high_spent_amount = dict_2[i]
            high_spent_date =  i
    output_summary += f"Highest Speding Day : {high_spent_date}, Amount : {high_spent_amount} \n"

    return output_summary

def write_summary(summary,filename):
    path = os.getcwd()
    new_path = os.path.join(path,filename)

    with open(filename , 'w') as file:
        file.write(summary)
    print(summary)


data = read_expenses('marks.csv')

output_summary = calculat_summary(data)

write_summary(output_summary,'monthly_summary.txt')


