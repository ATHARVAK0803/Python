#list:used to stroe multiple item in single variable
'''
#creating list
emp=["Sam","Ram","Shyam","Ghanshyam"]
stud=[1,"Ramesh","maland","O grade"]

print(emp)
print("THe list of student record",stud)

#you can acess individual value using index
print(emp[0])
print(stud[2])
print(stud[-1])

#updating list
emp[2]="Ragahv"
print(emp)

stud.append("9 cgpa")#adding elements at the end
stud.insert(1,"suresh")
print(stud)

#for removeing elements

stud.remove("suresh") #it remove the specific value that we mentioned in list
print(stud)
stud.pop() #it remove last value in the list
print(stud)

'''

#create a list with five elements and find the greatest among it
#method 1
'''
num=[1,43,54,6,3]
greatest=max(num) #max() is used to find greatest value
print("the greaetest value is",greatest) 
'''
'''
num=[1,43,54,6,3]

max=num[0]

for i in num:
    if i>max:
        max=i
print("the maximum is",max)
'''

#create a list with five elements and find the minimum among it
'''
num=[43,1,54,6,3]
min=num[0]
for i in num:
    if i<min:
        min=i
print("the minimum no is",min)
'''
