#dictonary are use to store key value pair
#it do not allow duplicate value
'''
#creating dictonary
Empdp ={"ramesh":101,
        "sammer":109,
        "Raj":100
        }

print(Empdp)

country={
    "India":"Delhi",
    "Germany":"Berlin",
    "England":"london"
    }

print(country)
print(country["India"])

country["Italy"]="Rome"
print(country)


del country["Germany"]
print(country)
'''
'''
users=[
{"name": "Alice","email": "alice@example.com","active": True},
{"name": "bob", "email" : "bob@example.com","active":False},
{"name": "Charlie","email":"charlie@example.com","active":True},
]

#task : get the email adress of active user.

active_email=[x['email'] for x in users if x['active']]
print(active_email)
 '''
#frozen set
#frozen set is immutable

'''
A frozen set is an immutable version of a python set.
while elements of a set can be modified at any time,
elements of frozenset remain the same after creation.
this immutabilty makes frozenset useful as key in dictonaries or as
elements of other sets"
'''

#random dictonary
person ={"name":"John","age": 23,"sex":"male"}
fset = frozenset (person)
print("The frozen set is :",fset)






