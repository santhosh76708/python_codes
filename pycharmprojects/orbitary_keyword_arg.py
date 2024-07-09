#print the itema sequence mannner
# def person(**data):
#     print(data)
#     for k, v in data.items():
#         if k == 'fname' or k == 'lname':
#           print(k, ' :', v)
#         elif k == 'age':
#              print(k, '   :', v)
#         else:
#            print(k, ':',v)
#
# person(fname='santhosh', lname='rathnam', age= 21, mobile= 93909)
#print items
# for k, v in data.items():
#     print(k, ':', v)

# def profile(**data):
#     print(data)
#     print('')
#     for k, v in data.items():
#         if k=='lname' or k=='nickn':
#             print(k,' :',v)
#         elif k=='branch':
#           print(k,':', v)
#         elif k=='htno':
#             print(k, '  :', v)
#         else:
#             print(k, '   :', v)
                                               #important lean must

#profile(lname='santhosh',nickn='lucky',branch='cse',htno="5d5",vlg='skzr')

#taking input from user

# name=input("enter your name: ")
# nickn=input("enter your nick name:")
# branch=input("enter your branch:")
# htno=input("enter your H.TNO:")
# vlg=input("enter your netive place:")
# print('')

#repeat the process n times
# e=1
# while e !='0':
#
#     name=input("enter your name:")
#     nickn=input("enter your nick name:")
#     branch=input("enter your branch:")
#     htno=input("enter your H.TNO:")
#     vlg=input("enter your netive place:")
#     print('')
#     profile(lname='santhosh',nickn='lucky',branch='cse',htno="5d5",vlg='skzr')
#     print('')
#     e=input("enter 0 to exit or any key to continue:")
# print('')

#Sending Dictionary as an Argument
e=1
while e !='0':
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    c=a+b
    print("sum of two numbers is:",c)
e=input("enter 0 to exit or any key to continue:")
print('')