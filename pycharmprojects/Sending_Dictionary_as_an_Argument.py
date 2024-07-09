def printperson(data):
    for k, v in data.items():
        if k=='fname' or k=='lname':
            print(k,' :', v)
        elif k=='branch':
           print(k,':', v)
        else:
            print(k,'   :', v)



#creating a dictionary

mydata={'fname':'rathnam', 'lname':'sanhosh', 'branch':'cse', 'age':22}
printperson(mydata)