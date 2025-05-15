#Conditional Statements-use to validate input data

'''
if
if...else
if...elif...else
'''



#Example to check whether the person can vote or not
'''
age=int(input("Enter your age"))

if(age>18):
    print("you can vote")
else:
    print("you can not Vote")'''

#Wap to give bonus to the employee if his salary is less than 30000(5%)
'''
Salary = int(input("enter your salary"))
if (Salary>30000):
    bonus=(Salary*5)/100
    net_salary =Salary+bonus
    print("Your salary for this month",net_salary)
    
else:
    print("your slary is",Salary)
'''

#WAP to accept scores of two team and make decision who won the match
'''
team1=int(input("Enter the score of team 1 : "))
team2=int(input("Enter the score of team 2 : "))
if(team1>team2):
    print("team 1 has won the match")
elif (team1==team2):
    print("The match is tie:")
    
else:
    print("team 2 has won the match")'''

# Accept % from the user and make a deciion
'''
per=int(input("Enter your percentagee"))
if (per>=75):
    print("you will got O grade")
elif (per>=60):
    print("you will got A grade")
elif (per>=40):
    print("you will got B grade")
else:
    print("you are Failed")'''



#wap find the greatest among three:
'''

a= int(input("Enter First number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if(a>b and a>c):
    print(a,"is greater than ",b,"and",c)
elif(b>a and b>c):
    print(b,"is greater than ",a,"and",c)
else:
    (c,"is greater than",a,"and",b)'''
    
#Wap to check whether the number is even or odd
'''
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number,"is an even number.")
else:
    print(number," is an odd number.")'''



#wap to check whether the year is leap or not
'''
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year,"is not a leap year.")'''


#WAP to check whether The entered number is divisible by 5 or not

a=int(input("Enter the number you want: "))

if a%5 == 0:
    print(f"{a} is divisible by 5")
else:
    print(f"{a} is not divisible by 5")
