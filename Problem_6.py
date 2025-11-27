
import os

import json

path = os.getcwd()

new_path = os.path.join(path,'products.json')

paths = os.path.join(path,'invalid_calls.txt')

def validate_inputs(func):
    def function(*args, **kwargs):
        with open(paths,'a') as file:
            try:
                if len(args) == 3:
                    id = int(args[0])
                    name = args[1]
                    price = float(args[2])
                    if len(name)==0:
                        file.write("Error: Product name cannot be empty.\n")
                        return 
                else:
                    id=int(args[0])
                    price=float(args[1])
                    
            except:
                file.write("Error: Invalid data type or missing required values.\n")
                return 

            if id<=0:
                file.write("Error: Product ID must be a positive integer greater than 0.\n")
                return 

            if price<0:
                file.write("Error: Product price cannot be less than 0.\n")
                return 
        
        return func(*args,**kwargs)
    return function


def read_data():
    try:
        with open(new_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        with open(new_path, "w") as file:
            file.write("[]")
        return []


@validate_inputs
def add_product(id,name,price):

    data = read_data()

    for i in data :
        if i['id'] == int(id) :
            return 
    product_data = {}
    product_data['id'] = int(id)
    product_data['name'] = name
    product_data['price'] = float(price) 
        
    data.append(product_data)

    with open(new_path, "w") as file:
       json.dump(data, file, indent=4)



@validate_inputs
def update_product(id,new_price):
        
    data = read_data()

    for i in data:
        if i['id'] == id:
            i['price'] = new_price

    with open(new_path, "w") as file:
       json.dump(data, file, indent=4)



while True:
    print("1.Adding Product \n2.Updating Product")
    choice = int(input("Eenter your choice : "))
    if choice == 1:
        id = input("Please enter the unique Product ID: ")
        name = input("Enter the product name (cannot be empty): ")
        price = input("Specify the price of the product: ")
        add_product(id,name,price)

    elif choice == 2:
        id=input("Enter Product Id : ")
        price=input("Enter Updated Price")
        update_product(id,price)
    
    elif choice == 3:
        print("-------------------Completed--------------------")
        break
    else:
        print("Enter Valid Input !!!")
