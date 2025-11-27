
# # 1.	Create a Simple Class
# #     Define a class Car with attributes brand and color. Create two objects and print their details.

# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#         print(f"Brand Name :{self.brand}" )
#         print(f"Color : {self.color}")      
#         pass

# obj1 = Car("BMW" , "Blue")
# obj2 = Car("Thar" , "Black")

# # 2.	Default and Parameterized Constructor
# # 	Build a Book class that sets default values if no parameters are passed.

# class Book :
#     def __init__(self,name="Jack"):
#         self.name = name 
#         print(f"Hello {self.name},Welcome to Class")
#         pass

# obj = Book("Monk")
# obj = Book()

# # Create a class Student with name and marks. Add a method grade() that prints "Pass" if marks ≥ 40 else "Fail".

# class Student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks 
#     def grade(self):
#         if self.marks >= 40 :
#             print(f"{self.name} you are Pass")
#         else:
#             print(f"{self.name} you are Fail")

# obj1 = Student("Jack",59)
# obj1.grade()

# obj2 = Student("Monk",15)
# obj2.grade()

# # Class Dog with class attribute species = "Canine" and instance attributes name, age. Show how changing species affects all instances.
# # Focus: Difference between instance and class variables.

# class Dog:
#     species = "Canine"
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
    
#     def display(self):
#         print(f"Name : {self.name}, Age : {self.age}, Species : {self.species}")

# obj = Dog("Jack",22)
# print(obj.name)
# print(obj.age)
# print(obj.species)
# # obj.display()


print("====================================================================")

# # Level 2 - Moderate Logic Building

# # Account Simulation
# #     Class Account with balance, deposit(), withdraw(), and show_balance() methods.
# #     Focus: State management and updates inside objects.

# class Account:
#     def __init__(self,balance):
#         self.balance = balance 
#         pass

#     def deposit(self,amount):
#         self.balance += amount
    
#     def withdraw(self,amount):
#         self.balance -= amount 
    
#     def balance_amount(self):
#         print(f"Balance Amount : {self.balance}")

# obj = Account(5000)
# obj.deposit(1000)
# obj.balance_amount()
# obj.withdraw(250)
# obj.balance_amount()



# # 6.	Shopping Cart
# #   Class Cart → methods to add_item(name, price), remove_item(name), and total_amount().


# class Cart:
#     def __init__(self,cart_item):
#         self.cart_item = []
        
#         pass 
#     def add_item(self,name,price):
#         item_dict = {}
#         item_dict['name']=name 
#         item_dict['price']=price 
#         self.cart_item.append(item_dict)
#     def remove_item(self,name):
#         for i in self.cart_item:
#             if i['name']==name:
#                 self.cart_item.remove(i)
#     def total_amount(self):
#         total = 0
#         for i in self.cart_item:
#             total += i['price']
#         print(f"Total Amount : {total}")
# obj = Cart([])
# obj.add_item("Phone",2500)
# obj.add_item("watch",300)
# obj.remove_item("watch")
# obj.total_amount()

# # Class Employee(name, salary) → method apply_bonus(percent) to update salary.

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary 
#     def apply_bonus(self,percent):
#         self.salary += self.salary * percent / 100
#         print(f"Name : {self.name} Salary : {self.salary}")

# obj = Employee("Monk",25000)
# obj.apply_bonus(20)

# # Class Temperature with methods to convert between Celsius ↔ Fahrenheit.
# # Focus: Understanding of function return values vs print.

# class Temperature:
#     def __init__(self,temperature):
#         self.temp = temperature
    
#     def cel_fah(self):
#         fah = (self.temp * 9/5 ) + 32
#         return fah
    
#     def fah_cel(self):
#         cel = (self.temp - 32 )*5/9 
#         return cel 

# obj = Temperature(250)
# print(obj.cel_fah())
# print(obj.fah_cel())



# # Class Student has list of marks. Method average(), and method result() → “Distinction”, “Pass”, or “Fail”.
# # Focus: Lists as attributes, control flow.

# class Student:
#     def __init__(self,marks):
#         self.marks = marks 
    
#     def average(self):
#         total_marks = 0
#         for i in self.marks:
#             total_marks += i
#         average_marks = total_marks / len(self.marks)
#         return average_marks

#     def result(self):
#         for i in self.marks:
#             if i<40:
#                 return "Fail"
#         return "Pass"

# obj = Student([41,56,78,93,95,57,86,48,22])
# print(f"Average {obj.average()}")
# print(f"Distinction : {obj.result()}")


# # ATM class with a PIN system, allows login, deposit, withdraw, check balance (validate PIN).
# # Focus: Simple access control logic using class state.

# class ATM:
#     def __init__(self):
#         self.pin = 5673
#         self.balance = 5600
    
#     def evaluate_pin(self,pin):
#         if self.pin == pin:
#             return True
#         return False

#     def deposit(self,amount):
#         self.balance += amount

#     def withdraw(self,amount):
#         self.balance -= amount

#     def check_balance(self):
#         return self.balance

# obj = ATM()
# pin = int(input("Enter you Pin : "))

# if obj.evaluate_pin(pin):
    
#     print("Adding Amount 250 ")
#     obj.deposit(250)
#     print(f"Balance {obj.check_balance()}")

#     print("Wtihdrawing Amount of 500")
#     obj.withdraw(500)
#     print(f"Balance : {obj.check_balance()}")
# else:
#     print("Pin is Incorrect. Plesae try again")


