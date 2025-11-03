
# # # # # # # # # # # # # # # name = "Jack"
# # # # # # # # # # # # # # # age = 21
# # # # # # # # # # # # # # # favoutie_hobby = "Playing Cricket"

# # # # # # # # # # # # # # # print(f"Name: {name}, Age: {age}, Hobbies: {favoutie_hobby}")

# # # # # # # # # # # # # # n = 10 
# # # # # # # # # # # # # # print("*" *n)
# # # # # # # # # # # # # # for i in range(n-2):
# # # # # # # # # # # # # #     print("*" + " "*(n-2) + "*")
# # # # # # # # # # # # # # print("*" *n)

# # # # # # # # # # # # # # num1 = 100 
# # # # # # # # # # # # # # num2 = 10.23 
# # # # # # # # # # # # # # num3 = "Hello"
# # # # # # # # # # # # # # num4 = True 
# # # # # # # # # # # # # # num5 = [1,2,3,4,5,67,8]
# # # # # # # # # # # # # # num6 = (1,2,3,4,5,6,7)
# # # # # # # # # # # # # # num7 = {'name':'Jack','Age':21}
# # # # # # # # # # # # # # print(type(num1))
# # # # # # # # # # # # # # print(type(num2))
# # # # # # # # # # # # # # print(type(num3))
# # # # # # # # # # # # # # print(type(num4))
# # # # # # # # # # # # # # print(type(num5))
# # # # # # # # # # # # # # print(type(num6))
# # # # # # # # # # # # # # print(type(num7))


# # # # # # # # # # # # # num1 = 10
# # # # # # # # # # # # # num2 = 20
# # # # # # # # # # # # # print(f"Before Swap Number1 : {num1}, Number2 : {num2}")
# # # # # # # # # # # # # nums_sum = num1+num2
# # # # # # # # # # # # # num2 = nums_sum - num2
# # # # # # # # # # # # # num1 = nums_sum - num1
# # # # # # # # # # # # # print(f"After Swap Number1 : {num1}, Number2 : {num2}")

# # # # # # # # # # # # # user_input = bool(input("Enter Anything : "))
# # # # # # # # # # # # # print(user_input)
# # # # # # # # # # # # # print(type(user_input))

# # # # # # # # # # # # # num1 = int(input("Enter the Radius of circle : "))
# # # # # # # # # # # # # area = 3.14 * (num1 * num1)
# # # # # # # # # # # # # print(f"Area of Cirlce is {area}")

# # # # # # # # # # # # principle = int(input("Enter Principle Amount : "))

# # # # # # # # # # # # time = int(input("Enter Time Period : "))

# # # # # # # # # # # # interest = int(input("Enter the Rate of Interest : "))

# # # # # # # # # # # # simple_interest = ( principle * time * interest ) / 100

# # # # # # # # # # # # print(f"Simple Interest Amount : {simple_interest}")

# # # # # # # # # # # num = int(input("Enter a Number : "))

# # # # # # # # # # # if num>10 and num<50:
# # # # # # # # # # #     print(f"{num} is between 10 and 50")
# # # # # # # # # # # else:
# # # # # # # # # # #     print(f"{num} is not between 10 and 50")

# # # # # # # # # # marks = int(input("Enter Marks : "))
# # # # # # # # # # attendance = int(input("Enter Attendance percentage : "))
# # # # # # # # # # if marks>=40 and attendance>=75:
# # # # # # # # # #     print("Passed")
# # # # # # # # # # elif attendance<75 and marks>=40:
# # # # # # # # # #     print("Failed due to Less attendance")
# # # # # # # # # # else:
# # # # # # # # # #     print("Failed due to marks less than 40")

# # # # # # # # # num1 = int(input("Enter Number 1 : "))
# # # # # # # # # num2 = int(input("Enter Number 2 : "))
# # # # # # # # # num3 = int(input("Enter Number 3 : "))

# # # # # # # # # num1 += num2*num3 
# # # # # # # # # print(num1)

# # # # # # # # num = int(input("Enter Number: "))
# # # # # # # # if num > 0:
# # # # # # # #     print("Positive")
# # # # # # # # elif num<0:
# # # # # # # #     print("Negative")
# # # # # # # # else:
# # # # # # # #     print("Zero")


# # # # # # # num1 = int(input("Enter Number1 : "))

# # # # # # # num2 = int(input("Enter Number2 : "))

# # # # # # # opr = input("Enter Operation : ")

# # # # # # # if opr == '+':
# # # # # # #     print(f"Addition : {num1+num2}")

# # # # # # # elif opr =='-':
# # # # # # #     print(f"Subtraction : {num1-num2}")

# # # # # # # elif opr == '*':
# # # # # # #     print(f"Multiplication : {num1*num2}")

# # # # # # # elif opr == '/':
# # # # # # #     print(f"Division : {num1/num2}")
# # # # # # # else:
# # # # # # #     print(f"floor Division : {num1//num2}")

# # # # # # year = int(input("Enter Year : "))

# # # # # # if ( year%4==0 and year%100!=0 ) or year%400==0 :
# # # # # #     print(f"{year} is Leap Year")
# # # # # # else:
# # # # # #     print(f"{year} is Not a Leap Year")

# # # # # name = input("Enter Your Name : ")

# # # # # age = int(input("Enter Your Age : "))

# # # # # area = input("Enter Your Area : ")

# # # # # print(f"Hi {name}, You age is {age} and you live in {area}")


# # # # lst = [1,2,3,4,5,6,7,8,9]
# # # # print(lst)
# # # # lst.append(10)
# # # # print(lst)
# # # # lst[8]= 100
# # # # print(lst)
# # # # lst.remove(2)
# # # # print(lst)

# # # lst = [1,2,3,4,5,6,7,8,9]

# # # total = 0
# # # maxx = 0
# # # minn = 100
# # # for i in lst:
# # #     if maxx<i:
# # #         maxx = i
# # #     if minn>i:
# # #         minn = i
# # #     total += i 

# # # print(f"Maximum : {maxx}")
# # # print(f"Minimum : {minn}")
# # # print(f"Sum : {total}")
# # # print(f"Average : {total/len(lst)}")


# # lst = [1,1,3,4,6,7,8,0,8,9,4,6,3,2,4,5,6,8,6,9,0,5,2,1]
# # res_lst = []
# # for i in lst:
# #     if i not in res_lst:
# #         res_lst.append(i)
    
# # print(res_lst)

# # tup = (1,[1,2,3],3,4,5,6,7,8,90)

# # tup[1].append(11)

# # print(tup)



# student_details = {"name":'Jack' , 'age' : 21 , 'marks' :95}
# for i in student_details:
#     print(i , student_details[i])

# student_details['age'] = 51 

# print(student_details)

# del student_details['marks']

# print(student_details)

# sentence = "Hi Jack Welcome to Meet Jack and his Friends and welcome jack"

# dict_items  = {}

# for i in sentence.split():
#     if i.lower() in dict_items:
#         dict_items[i.lower()]+=1
#     else:
#         dict_items[i.lower()] = 1

# print(f"Final Dictionary : {dict_items}")


# set_1 = [1,10,9,4,3,5,6,7]
# set_2 = [11,12,1,3,14,5,6,7,8]

# set_1.extend(set_2)

# set_final = set()
# for i in set_1:
#     if i not in set_final:
#         set_final.add(i)

# print(f"Final set : {set_final}")


# for i in range(1,10):
#     print(f"=====================  Multiplication table of {i}  =============================")
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)

# print(fact(5))


# def largest_number(a,b,c):
#     if a>b:
#         if a>c:
#             return f"{a} is Largest Number"
#         else:
#             return f"{c} is Largest Number"
#     else:
#         if b>c:
#             return f"{b} is Largest Number"
#         else:
#             return f"{c} is Largest Number"
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# num3 = int(input("Enter third Number : "))
# print(largest_number(num1,num2,num3))

