
# # # basic calculater
# print("what you want to do?\n1 for addition \n 2 for subtraction \n 3 for multi \n 4 for div")
# a_1=int(input("enter the digit"))
# a_2=int(input("enter digit 1"))
# a_3=int(input("enter digit 2")) 
# if(a_1 == 1):
#     print("addition is " ,(a_2+a_3))
# elif(a_1 == 2):
#     print("addition is " + str(a_2-a_3))
# elif(a_1 == 3):
#     print("addition is " + str(a_2*a_3))
# elif(a_1 == 4):
#     print("addition is " + str(a_2/a_3))
# else:
#     print("wrong input")

##Lists

# my_list=["vibhu","dev","ansh","amit","gattu"]
# my_numbers=[2,3,4,1,5]

# print(my_list[3])
# print(my_list.append("savani saap"))
# print(my_list)
# print(my_list.extend(my_numbers))
# print(my_list)
# print(my_list.insert(2,"pratik"))
# print(my_list)
# print(my_list.count("vibhu"))
# # print(my_list.remove("vibhu"))
# # print(my_list)
# # print(my_list.pop()) #it will return the element poped out
# # print(my_list)
# # print(my_list.clear())
# # print(my_list)
# print(my_list.index("vibhu"))
# print(my_list.sort())
# print(my_list)
# print(my_list.reverse())
# print(my_list)
# my_list_2=my_list.copy()
# print(my_list_2)
# my_list_2.append("darpi")
# print(my_list)
# print(my_list_2)

###tuples

# my_list=[("vibhu","hi"),("dev","jm"),("ansh","amit")]
# print(my_list.append([2,"hii"]))
# print(my_list)

# #function

# def my_funct1(vi,age):
#     print("heelo"+str(age)+"hmm",vi)
# my_funct1(4,4)

#if 

# tall_1=False
# big=False 
# if tall_1 and big:
#     print("you are both tall and big")
# elif tall_1 and not(big):
#     print("ypu are tall not big")
# elif not(tall_1) and big:
#     print("you are not tall but big")
# else:
#     print("you are not tall and not big")

#dictionary

# dict_1=(1,23,4,)
# dict_2=(2,2,2,34)
# x=dict.fromkeys(dict_2,dict_1)
# print(x)
# dict_3={"hi":"helo",2:23,"hmm":[1,2],[1,2]:[1,2]}
# print(dict_3)
# ##for loops

# my_list=([1,2,3],[4,5,6],[7,8,9])
# for i in my_list:
#    print(i)

# exponent function

# 2^3
# def power_function(num1,num2):
#     x=1
#     for i in range(num2):
#         x=num1*x
#     return x        
         
# for i in range(5):
#     print(i)     


# num_1=int(input("enter the number :"))
# num_2=int(input("enter the power of number :"))
# y=power_function(num_1,num_2)
# print("the output is",y)

#translator

# def translator(phrase):
#     translation=""
#     for i in phrase:
#         if i in "aeiouAEIOU":
#             if i.isupper():
                 
#              translation=translation + "G"
#             else:
#                translation=translation + "g"
        
#         else:
#             translation=translation + i
#     return translation

# print(translator(input("enter the phrase ")))

# # try and catch error

# try:
#     my_value=10*9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999990
#     print(my_value)
#     x=int(input("enter the input"))
#     print(my_value/x)
# except ArithmeticError:
#     print("wrong input")

# import pandas as pd 
# file_path = 'vibhu.txt'
# x=pd.read_csv(file_path,delimiter='\t')
# # print(x)
# with open('vibhu1.txt', 'r+') as file:
#     # Reading content from the file
#     content = file.read()
#     print("Content before modification:")
#     print(content)

#     # Repositioning the file pointer to the beginning
#     # file.seek(0)

#     # Writing new data
#     file.write("vibhu patel")

#     # Truncating the file to the current position (removing any remaining old data)
    
def roll(num):
    x=num*3
    return x;
meter=20
liter=45