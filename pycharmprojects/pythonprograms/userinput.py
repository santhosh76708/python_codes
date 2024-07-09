# x = input("Enter 1st number :")
# y = input("enter 2nd number :")
# a =int(x)
# b =int(y)
# z= a+b
# print("sum of two numbers is :",z)

#withou using a,b we can directly convert

# x = int(input("Enter 1st number :"))
# y = int(input("Enter 2st number :"))
# z=x+y  #//use + , - , * , /, %
# print(z)  #output is 80
# print()

#if you want print paricular a charecter in a string use this:---

name =input("enter any char :")
#if len(name)!=1:  // when u use for loop that gives limited choices and gives wrong
while len(name)!=1: #when your using while loop that gives ,utiple choices until enter currect response
    print("enter only one char :")
    name =input("enter any char :")
    print(name)
# x = name
# print(x[4])
# count = len(name)
# print(count) 