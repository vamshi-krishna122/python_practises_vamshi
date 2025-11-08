
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


