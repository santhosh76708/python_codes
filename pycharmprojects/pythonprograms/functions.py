# def sayhello():
#     print("hello santhu")
#     print("Gd morning")
#     print("This is my python functions session")

# sayhello()

# print("\n abcdefghijklmnopqrstuvwxyz \n")

# sayhello()

#Dynamically change the details

# def sayhello(name):
#     print("Hello", name)
#     print("good morning!")
# sayhello("santhosh")    

#creating variable and that value store in the function

# def sayhello(name):
#     print("hellow", name)
#     print("Good morning!")
# user_name="santhosh" 
# sayhello(user_name)
# sayhello("lucky")


'''default arguments ...when we are using name=user that time 
not showing any types of erreor other whise that show some error'''

# def sayhello(name = "user"):
#     print("hello", name)
#     print("good morming")
# sayhello("bakki")  #bakki that direct access the user 


#add function

#def add(a , b):
   #  result = a + b
    # x= int(result)

    # print ("sun of two numbers:", +x)
    # print("sum of two numbers:", result)
    
#when we are using + that time take direct string
    
#     print("sum of two numbers:", str(result))
# add(34 , 65)
# add(44 , 65)
# add(94 , 65)


#taking unlimted inputs/Arguments
# def getSum(*x):
#     result =0
#     for a in x:
#         result +=a
#     print("result :", result)
# getSum(23,5,2,8,9,10)      
   # print(x[2]) #using index print the elements
#getSum(23,5,2,8,9,10)  
#add(23,87)


def sayhello(name,age): #formal Arguments
    print("your name is :",name)
    print("your age is :",age)

#sayhello("santhosh",21)   

    #if any chance you forget the functions sequence use this directly

sayhello(age=21, name="santhosh")  #actual arguments