import os


def write_summary(final_dict):
    output = ""
    for i, info in sorted_dict.items():
        output += (
            f"Student Id: {i}\n"
            f"Name: {info['student_name']}\n"
            f"Average Marks: {info['average']}\n"
            f"Highest Scored Subject: {info['Max']}\n"
            f"Lowest Scored Subject: {info['Min']}\n"
            "-----------------------------------\n"
        )
    return output


def calculate_operations(final_dict):
    for i in final_dict:
        average = final_dict[i]['subject_marks']
        max_subject =""
        min_subject = ""
        max_subject_marks =0
        min_subject_marks =  1000000007
        for idx in average.keys():
            if average[idx] > max_subject_marks:
                max_subject_marks = average[idx]
                max_subject = idx
            
            if average[idx] < min_subject_marks:
                min_subject_marks = average[idx]
                min_subject = idx
            
        final_dict[i]['Max'] = max_subject
        final_dict[i]['Min'] = min_subject
    return final_dict

path = os.getcwd()
new_path = os.path.join(path,'marks.txt')

file = open(new_path, 'r')
values = []
data = file.readlines()
info = list(data[0].replace("\n","").split(","))
for i in range(1,len(data)):
    values.append(data[i])


values_array = []
for i in values:
    values_array.append(i.replace("\n","").split(","))

final_dict={}
for i in values_array:
    dict_1 = {}
    if final_dict.get(i[0])==None:
        dict_1['student_name']= i[1]
        dict_1['subject_marks'] = {i[2]:int(i[3])}
        dict_1['average']=int(i[3])
        final_dict[i[0]]=dict_1
    else:
        final_dict[i[0]]['subject_marks'][i[2]]=int(i[3])

operation_dict = calculate_operations(final_dict)

sorted_dict = dict(
    sorted(operation_dict.items(), key=lambda x: x[1]['average'], reverse=True))

file.close()

new_path = os.path.join(path,"result.txt")

file1 = open(new_path,'w')

output_ans = write_summary(sorted_dict)

file1.write(output_ans)

file1.close()

# import os 

# path = os.getcwd()

# new_path = os.path.join(path,'marks.txt')

# file = open(new_path , 'r')

# data = file.readlines()

# print(f"Number of Lines in {len(data)} , Type : {type(data)} ")