
import os

path = os.getcwd()

new_path = os.path.join(path,'emplyee.txt')

summary_text = "performance_summary.txt"

error_text = "error_log.txt"

def read_file():
    try:
        with open(new_path,'r') as file:
            data = file.readlines()
            return data
    except:
        print("File Not Found In the Location")
        return 


def verify_data(data):
    input_fields = data.split(",")

    error_path = os.path.join(path, error_text)

    def write_error(msg):
        with open(error_path, 'w') as file:
            file.write(msg)
        return None

    if len(input_fields) != 4:
        return write_error("Data Fields are missing in the input.")

    emp_id, name, dept, rating = input_fields

    if not emp_id.isdigit():
        return write_error("Employee ID should be a number.")

    if not name:
        return write_error("Name field cannot be left empty.")

    if not dept:
        return write_error("Department must be provided.")

    try:
        rating = float(rating)
        if not (1.0 <= rating <= 5.0):
            return write_error("Rating must be between 1.0 and 5.0.")
    except ValueError:
        return write_error("Rating is Not in Format of Floating Value")

    return [int(emp_id), name, dept, rating]


    
def validate_data(data):
    valid_data= []
    for i in data:
        res = verify_data(i)
        if res is not None:
            valid_data.append(res)
    return valid_data

def summary_data(data):

    sum_rating_dpet = {}
    count_dept={} 
    top_performance = 0

    for i in data:
        if i[2] in count_dept:
            sum_rating_dpet[i[2]]+=i[3]
            count_dept[i[2]]+=1  
        else:
            count_dept[i[2]]=1
            sum_rating_dpet[i[2]]=i[3]
        if top_performance < i[3]:
            top_performance = i[3]
    
    performance_summary = ""

    performance_summary += f"Total Valid Employees :  {len(data)} \n"

    performance_summary += "Average Ratings By Department  \n"

    for i in count_dept:
        performance_summary += f"{i} : {sum_rating_dpet[i] / count_dept[i]}\n"

    performance_summary += "Top Performer \n"

    for i in data:
        if i[3] == top_performance:
            performance_summary += f"Employee Name : {i[1]} \n"
            performance_summary += f"Department : {i[2]} \n"
            performance_summary += f"Rating : {i[3]}\n"

    performace_path = os.path.join(path,summary_text)
    
    with open(performace_path,'w') as file:
        file.write(performance_summary)
    
data = read_file()

if data is not None:
    valid_data_input = validate_data(data)
    summary_data(valid_data_input)

