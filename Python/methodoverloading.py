#method overloading

'''Use of some method name with diff parameter in a single program is calle as method overloading
'''
'''
class MethodOver:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

obj=MethodOver()
#print(obj.add(45,56))
ans=obj.add(67,35,76)
print("the output is:",ans)
'''

#solution 1 : this problem can be avoideed by using default arguments
#solution 2: we can achieve mathod overloading by adding variables args concepts(*args)
'''
class MethodOver:
    def add(self,*args):
        total =0
        for i in args:
            total=total+i
            return total
obj=MethodOver()
print(obj.add(45,56))
print (obj.add(45,8,67,88))
ans=obj.add(67,34,76)
print("The output is ",ans)
print(obj.add(4,6,7,8,9,2,1,10,3,5))
   
'''

#static mthod is a method which gets called through classname
#(we dont use object here)

class StatDemo:
    @staticmethod
    def greet():
        print("Hello World")

StatDemo.greet()
obj=StatDemo()
obj.greet()
