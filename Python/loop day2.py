#wap to reverse a number 123 to 321
'''
n= int(input("Enter the number: "))
original=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10   #floor division
    print(rev)
print("The reverse of a number is",rev)
'''

#wap to check no is palindrome or not
    
'''
n= int(input("Enter the number: "))
original=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10   #floor division
    print(rev)
print("The reverse of a number is",rev)
if original == rev:
    print("the given number is a palindrome")
else:
    print("the given no is not a palindrome")'''


#wap to get sum of digit in user input
'''
n= int(input("Enter the number: "))
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print(f"the sum of the no is",sum)'''


#wap to check armstrong number

n= int(input("Enter the number: "))
order=len(str(n))
sum=0
temp=n
while n>0:
    rem=temp%10
    sum+=rem**order
    temp//=10
if n==sum:    
    print("the number is armstrong number")

else:
    print("the number is not armstrong number")
