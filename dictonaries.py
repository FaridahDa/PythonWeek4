hello = 'hi'
mydict = {'Australia': 'Canberra', 'Nigeria' : 'Lagos', 'US': 'Washington'}
print(mydict['Nigeria'][2])

homer = 1
print(mydict['US'][homer])

mydict['NG']= {'Lagos', 'Ibadan', 'Abuja'}
for country in mydict.keys() :
    print(country,':' , mydict[country])

