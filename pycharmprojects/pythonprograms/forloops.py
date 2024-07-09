# #For Loop Syntax:

# '''for iterator_var in sequence:
#     statements(s)'''

# #example small problem

# n = 4
# for i in range(0, n):
#     print(i)

#i'm using [] so its gives sequence order name
'''persons = ['santhosh','lucky','bakki','supriya']
for users in persons:
    print(users)'''


    #if i'm using {} this gives unorder names
'''persons = {'santhosh','lucky','bakki','supriya'}
for users in persons:
    print(users)'''

#if you print charecter by charecter in a string using for  lopp
'''name = "santhosh"
for x in name:
    print(x) #o/p----> s a n t h o s h  //vertical


#if any chance stop the printing particular charecter use this
    if x == "t":
        break  #s a n t //vertical'''





frds = ['naveen','lucky','balu','sandeep']
for user in frds:
    if user == "balu":
        continue #if you use continue thats leaves name and continue the loop
    print(user)



