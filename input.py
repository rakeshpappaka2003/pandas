"""name = input("enter the name ")
age = int(input("enter the age "))
address = input("enter the address")
print("my name is:",name)
print("my age is:",age)
print("my address is:",address) """  #get for variable name age , address.print it
 


"""a = int(input("enter the a value:"))
b = int(input("enter the b value:"))
c = int(input("enter the c value:"))
d = a*b*c
e = a+b+c
f = d/e
print(f)"""            #get integer input for variable a,b,c
                          # multiply all three variables(a*b*c)
                          # add all three variables(a+b+c)
                          # divide the mul value by add value print it 




"""name = input("enter the name:")
score = int(input("enter the sore:"))
department =input("enter the department:")
marks = score/10
print("my name is:",name)
print("my score is:",marks)
print("my department is:",department)"""         #get input for variables name ,score , department
                                               # get score 


# implicit and explicit 

"""a = 24
b = 30.0
print(a+b)    #implicit                                        
print(int(a+b))"""  #explicit

"""print('my depart\'s')
print("my depart\"s")
print("my depart\'s")"""



"""print("hello\world")
print("hello\nworld")     # \n means new line
print("hello\tworld")     # \t means space
print("hello\bworld")     # \b means one step backspace remove one number
print("name\tid\tstudentno")    # it shows row but row distance not same (\t)
print("name\tid\t\bstudentno")   # it use \b rows distance all same
print("hello\rworld")           # \r means replace 
print("hello\rrakesh")
print("abcd\refg")
print("raki\rraja")
print("rakes\rloke")
print("234\v2343")                    # \v it executes pyramid shape
print("hi\vhello\vrakesh") """      

"""a = "rakesh"
print(a[0:3])
print(a[-6:-2])
print(a[-6:-8])
a = "hello"
print(a[0:5:1])
print(a[0:5:2])
print(a[0:5:3])
a = "helloworld"
print(a[2:9:2])


name="Vamsi"
print(name[::-1])
name = "rakesh"
print(name[::-1])"""



"""if True :
    print("hI")
if False :    
    print("hi")
else:
    print("bye")"""

"""age = int(input("enter the age"))
if age>=18:
    print("eligible")
else:
    print("not eligible ")""" 

"""num = int(input("enter the values"))
if num>0:
    print("positive")         
elif num<0:
    print("negative")    
else:
    print("0") """

"""num = int(input("enter the value"))       
if num%2==0:
    print("even") 
else:
    print("odd")  """


"""num = int(input("enter the value"))
if num%2==1:
    print("odd")
else:
    print("even")   """

"""a =int(input("enter the nu"))
if a>=1000:
    discount=a*10/100
    finalbill=a-discount
    print(discount ,finalbill)
else:
    print("no") """

"""a =int(input("enter the nu"))
if a>=1000:
    discount=a*10/100
    print(discount)
else:
    print("no") """


"""a = int(input("enter the a value")) 
b = int(input("enter the b value"))
c = int(input("enter the c value"))  
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")    
else:
    print("c is greater")"""

"""a = int(input("enter the a value"))
b = int(input("enter the b value"))
c = int(input("enter the c value"))        
d = int(input("enter the d value"))
if a>b and a>c and a>d:
    print("a is greater")
elif b>a and b>c and b>d:
    print("b is greater")    
elif c>a and c>b and c>d:
    print("c is greater")
else:
    print("d is greater")""" 

"""a = int(input("enter the value a"))
b = int(input("enter the value b"))
if a>b:
    print("a is greater")
else:
    print("b is greater")  """

"""marks = int(input("enter the value a"))
if marks>=90:
    print("a grade")
elif marks>=80:
    print("b grade")    
else:
    print("c grade") """

"""vowels = input("enter the values")
if vowels in ("a,e,i,o,u"):
    print("vowels")
else:
    print("constants") """

"""year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it is leaf year")
else:
    print("not leaf year")"""

"""if 4==0 and 4!=0 and 4<=0 or 4>=0:
    print("hello") 
else:
    print("bye")"""

"""a = int(input("enter the year"))
if a%400==0:
    print("a is leap year")
elif a%100==0:    
    print("a is leap year")
elif a%4==0:
    print("a is leap year")
else:
    print("a is not leap year")   """           

""""x = int(input("enter the num"))
result = "zero" if x == 0 else "positive" if x > 0  else "negative"
print(result)"""

"""raining = True
while raining:
    print("rakesh")
    raining = False"""

"""count = 0
while count<=5:
    print(count)
    count +=1"""

""""a = 0
while a<=100:
    print(a)
    a = a+2     #even 

a = 1
while a<=100:
    print(a)
    a = a+2 """ #odd


"""for i in range(6):
    print(i)"""

"""count =1
while count<=10:
    print("5","*",count,"=",5*count)
    count=count+1"""


""""y=int(input("enter a value"))
a = 1
while a<=10:
    print(y,"x",a,"=",y*a)
    a=a+1"""



"""a =1 
while True:
    print(a)
    a+=1"""

"""name = "rakesh"
print(f"hello {name}")

name = input("enter the nmae")
age = int(input("enter the age"))
address=input("enter the address")
print(f"my name is {name}\nmy age is {age}\nmy address is {address}")"""

"""i = 1
count=1
while count<5:
    if i%2==0:
        print(i)
        count+=1
    i+=1"""


"""i =5
count = 0
while count<=5:
    print(i)
    i=i-1
    count+=1"""
        

"""i =8
count = 1
while count<=5:
    if i%2==0:
       print(i)
    count+=1
    i=i+1 



i =8
count = 1
while count<=5:
    if i%2!=0:
       print(i)
    count+=1
    i=i+1 """

"""number=int(input("enter the number :"))
if number%2==0 and number%5==0:
    print("even and divisible ")
else:
    print("odd and divisible ")"""

"""ans = " "
while ans!="python":
    ans= input("enter the best program ")
print("correct")"""

"""for rakesh in range (10):
    print(rakesh)        #for loop 0 to 9

for i in range (1,4):
    print(i)

for i in range(0,5) :          #syntax   for variable in sequence:
    print (i)                       

for i in range(3):
    print("hello")

for i in range (3):
    print("hello",i)"""

"""for i in range (5):
    print(i%2==0)
    print(i*1) """

"""num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)"""

'''for i in range(5):
    print(i+2)'''

'''for i in range(5):
    print(i!=3)'''


'''for i in range(5):
    print(i*2)  '''
  
'''for i in range(5):
    print(i/2)  

for i in range(5):
    print(i+2)  

for i in range(5):
    print(i-2)  """

"""game=" "
while game!="cricket":
    game=input("enter the fav game:")
print("This is your fav game")"""

"""hobbies=" "
while hobbies!="reading":
    hobbies=input("enter your hobbi:")
print("this is your hobbi")"""

num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''

'''for a in range (5):
    for b in range (2):
        print("i'm  a=",a,"i'm b=",b)
        print()'''

'''for i in range (1):
    for j in range (2):
        print("i'm i:",i,"i'm j",j)'''

'''for i in range (5):
    for j in range (0,6,2):
        print(f"{i}{j} ",end=" ")
    print()'''

        
'''for i in range (5):
    for j in range (i):
        print("*")
    print()

for i in range (5):
    for j in range (i):
        print("*",end="")
    print()    '''

'''for i in range(1,6):
    if i == 3:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)'''



'''a=1
while a<=5:
    if a==3:
        #a=a+1
        continue
    print(a)
    a=a+1'''

'''a=1
while a<=5:
    if a==3:
        a=a+1
        continue
    print(a)
    a=a+1'''

'''n=5
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)

n = 5
for i in range (1, n+1):
    print("" * (n-1), end="")'''

'''for i in range (1,6):
    for j in range(1,6):
        print(f"{i}",j)
    print()'''

'''a = int(input("enter the a value"))
b = int(input("enter the b value"))
for i in range(a+1,b):
    print(i)'''

'''a = int(input("enter a value"))
b = int(input("enter b value"))
while a<b:
 print(a)
 a+=1  '''
 
'''empty_list=list()
print(type(empty_list))

list1 = [1, "hello", 2.5, True ]
list2 = [1, "hello", 2.5, True ]
print(list1==list2)'''

'''list1 = [1,"hello",[1,2,"hi"] ,4.5,True,[10,30]]
print(list1[5][1])'''

"""list1 = [1,"hello",[1,2,["a"],"hi"] ,4.5,True,[10,"rakesh"]]
print(list1[5][1][3])"""


"""a = " "
while a!="week1":
    a = input("enter a week:")
    for i in range(1,8):
        print("day",i)"""

"""empty_list=list()
print(type(empty_list))"""


"""list = [1,2, 3]
list .insert(2,5)
print(list)

list = [1,2,3,4,5,6]
list .insert(4,4)
print(list)"""

"""list = [1,2, 3]
list .append(4)
list .append(5)
print(list)              

list = [1,2,3, "hello"]
list .append(0)
print(list)"""

"""list = [1,3,3,2,4]
list .remove(4)
print(list)

list = [1,3,3,2,4]
list .remove(3)
print(list)"""

"""lst = [1,2,3,4]
x = lst.pop(3)  
print(lst)      #index type 0,1,2,3
print(x)   """


"""list = [10,20,30,40,]
print(list.index(10))"""  #index 10 is place in 0

"""list = [1,2,2,2,3,4,5]
print(list.count(2))

list = [1,2,2,2,3,4,5]      
print(list.count(1)) """ # which number  many times  comes in the list identify 


"""list = [1,2,3,5,4]
list.sort()
print(list) """#assending order 

"""list = [1,2,3,4,5]
list.reverse()
print(list)"""

"""list = [2.5,3,4,5]
for i in list:
    print(i)
    if i ==5:
       list.append(6)
print(list)"""
    
'''x = [2.5,2,3,5]
for i in range(5-len(x)):
    x.append(6)
    print(x)'''

#functions

"""def function_name():
    print("rakesh")
    print("rak")
function_name()"""

"""def add(a,b):
    return a+b
y= add(2,3)
print(add(2,3))"""

"""def reverse_string(x):
    y=x[::-1]                
    return y
print(reverse_string("rakesh"))"""

"""def name(r):
    if r==r[::-1]:
        return "true"
    else:
        return "false"
print(name("madam"))"""

"""def cal_fac(x):
   if x==0 or x==1:
        return 1
   else:
       result = x*cal_fac(x-1)
       return result
print(cal_fac(5))"""

"""list=[1,2,3,4,5]
list.append(6)
print(list)"""

'''a =[]
count=0
while count<=10:
    a.append(count)
    count+=1
print(a)

a =[1,2,3,4,5,6,7,8]
count=0
for i in a:
    count=count+1
print(count)'''
"""a=[]
for i in range(11):
    a.append(i)
print(a)"""


"""class hi(): #class name
    pass #placeholder
a = hi() #object"""
                                         #oops concept
"""class a():
    def add(self,a=2,b=3):
        print(a+b)
b = a()
b.add()"""

"""class class_name:
    def fun_name():
        print("hello")
    fun_name()
a=  class_name()


class class_name:
    def fun_name(self):
        print("hello")
a = class_name() 
a.fun_name() """ 




''''class laptop:
    def __init__(self):
        print("demo")
a = laptop()'''

"""class phone:
    chargetype="c-type"
    def __init__type(self,brand,price):
        self.brand=brand
        self.brand=brand
    def showdetails(self):
        print("brand",self.brand)
        print("price",self.price)
        print("chargetype",self.c-type)
samsung=( "vivo", "10000") """

"""class teacher():
    def __init__(self,name,reg_no):
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print("teacher name",self.name)
        print("reg_no",self.reg_no)
t1=teacher("rakesh",102)
t2=teacher("vamsi",122)
t1.display()
t2.display()  """

"""class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self)    :
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a // self.b
cal =calculator(10,5)
print("add",cal.add())
print("sub",cal.sub())
print("mul",cal.mul())
print("div",cal.div())"""


#in heritance

"""class a():
    def x(self):
        print("hello")
class b(a): 
    def y(self):
        print("rakesh")
obj=b()
obj.x()
obj.y()    """          

# multilevel inheritance

"""class a():
    def x(self):
        print("hello")
class b(a):
    def y(self):
        print("iam")        
class c(b):
    def z(self):
        print("rakesh") 
obj =c() 
obj.x()
obj.y()
obj.z()        

#multiple inheritence
class a():
    def x(self):
        print("hello")
class b():
    def y(self):
        print("iam")        
class c(a,b):
    def z(self):
        print("rakesh") 
obj =c() 
obj.x()
obj.y()
obj.z() """             


"""class animal:                          
    def speak(self):                              
     print("animal makes a sound")        # when you want extend the functionality or a parent class     
class dog(animal):                         without rewriting the same code
    def speak(self):                             it is especially useful in inheritance 
        super().show()                      once use another constructor super().the whole 
        print("dog barks")                  print statements exicute in the output 
d =dog()
d.speak()"""

"""class a:
    def show(self):
        print("class a")
class b(a):
    def show(self):
        super().show()
        print("class b")
class c(b) :
    def show(self):
        super().show()
        print("class c") 
d=c()
d.show()"""     


# Base class
"""class BankAccount:
    def _init_(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Current Balance: {self.balance}")
        else:
            print("Insufficient Balance!")

    def display(self):
        print(f"Account No: {self.account_number}, Name: {self.name}, Balance: {self.balance}")


# Derived class 1: Savings Account
class SavingsAccount(BankAccount):
    def _init_(self, account_number, name, balance=0, interest_rate=5):
        super()._init_(account_number, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}. New Balance: {self.balance}")


# Derived class 2: Current Account
class CurrentAccount(BankAccount):
    def _init_(self, account_number, name, balance=0, overdraft_limit=5000):
        super()._init_(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. Current Balance: {self.balance}")
        else:
            print("Overdraft Limit Exceeded!")


# --- Testing the program ---
# Savings Account Example
s1 = SavingsAccount("S101", "Raja", 1000)
s1.display()
s1.deposit(500)
s1.add_interest()
s1.withdraw(300)

print("\n")

# Current Account Example
c1 = CurrentAccount("C202", "Sekhar", 2000)
c1.display()
c1.withdraw(6000)  # within overdraft
c1.withdraw(8000)  # exceeds overdraft
"""

"""class dad():
    def money(self):
        print("dad's money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s1=son1()
s1.money()"""


"""class dad():
    def money(self):
        print("dad's money")

class land():
    def important(self):
        print("important")

class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s1=son1()
s1.money()
s1.important()"""

"""class room():
    def bench(self):
        print("wood type")
class window():
    def use(self):
        print("iron metal")
class room1( room,window):
    pass
class room2(room):
    pass
class room3(room):
    pass
r1=room1()
r1.bench()
r1.use()
r2 =room2()
r2.bench()
r3=room3()
r3.bench()"""

"""class student():
    def __init__(self,name,register_no):
       self._name =name
       self._register_no =register_no
    def display(self):
        print("name:",self._name)
        print("reg_no:",self._register_no)
obj=student("rakesh",1234576)
obj.display()"""

"""class Teacher():
    def _init_(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("Name:",self.name)
        print("ReG_num:",self.reg)
a=Teacher("MAM1",'1234')
b=Teacher("MAM2",'4567')
a.display()
b.display()"""

"""class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b!=0:  
         return self.a/self.b
        else:
         return "division"
v=cal(2,3)
print(v.add())
print(v.sub())
print(v.mul())
print(v.div())"""

"""class fruit():
    def _init_(self,color):
        self.color=color
    def display(self):
        print("Fruit colour name:",self.color)
obj=fruit("pink")
obj.display()"""

"""class company:
    def __init__(self):                   #encapsilation __
        self.__companyname="google"
    def display(self):
        print(self.__companyname)    

c1=company()
c1.companyname=("goooogle")
c1.display()"""

#polymorphism
"""
types
1. inbuilt polymorhism
2. method overloading(indirect)
3. object polymorhism
4. class polymorhism
5.method polymorhism"""

"""name="rakesh"
list1 = [1,2,3,4,5,6]    #inbuilt
print(len(name))
print(len(list1))"""

"""p = "123.567"
print(p[4::]+p[3]+p[0:3])"""   #method


"""def add(x):
    return x
def add(x,y):
    return x+y
def add(x,y,z):
    return x+y+z
print(add(1,2))"""
 

"""class addition:
    def add(x):
        return x
    def add(x,y):
        return x+y
    def add(x,y,z):
        return x+y+z
a = addition()
print(a.add(1,2,3))"""


"""class car():
    def wheel(self):
        print("it is good")
class bike():
    def wheel(self):
        print("it is bad")
    def size():
        print("it is small")    
    def details (obj):
        obj.wheel()
        obj.size()
obj=car("good")
obj.bike()
obj.size()"""


"""class animal():
    def _makesound_(self):
        print("animals make sound")
class dog(animal):                          #method overriding
    def _makesound_(self):
        print("dog barks ")
animal=animal()
dog = dog()
animal._makesound_()
dog._makesound_()

a = 2
b = 1
print(a+a)"""

"""from abc import ABC ,abstractmethod
class colleges(ABC):
    @abstractmethod
    def types(self):
        print("hello")
class Mcollege(colleges):
    def types(self):
        print("it is a betch")
class Ecollege(colleges):
    def types(self):
        print("it is a mtech")
m = Mcollege()
e = Ecollege()
e.types()        
m.types()"""

"""try:
    a=int(input("enter "))
    b=int(input("enter "))
    print(a+b)
except Exception as e:
    print(e)"""

"""
try:
    ifa = int(input("enter "))
    b = int(input("enter "))
    print(a+b)
except ValueError as e:
    print("name Error")
 
    try:
        a = int(input("enter "))
        b = int(input("enter "))
        print(a/b)
    except ValueError as e :
        print("name Error")  
    else:    
        try:
            a = int(input("enter"))
            b = int(input("enter"))
            print(a*b)
        except ValueError as e :
            print("nameError")"""

f=open("text_file.txt","w")
f.write("Grade")
f.close()
