
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=person('Ahmad',22)
print("name:",person1.name)
print("age:",person1.age)
#..............................................................................
2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello my name is :",self.name)
        print("the age is:",self.age)
person1=person("John",25)
person1.greet()
.....................................................................................
3
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def print_details(self):
        print(f"make:{self.make},model:,{self.model},year:,{self.year}")
car1=car("toyota","camry",2020)
car1.print_details()
..................................................................................
4
import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
circle1=circle(50)
print(circle1.area())
.........................................................................................................
5
class rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def compute_area(self):
        return self.width*self.lenght
    def compute_perimeter(self):
        return (self.width+self.lenght)*2
rectangle1=rectangle(12,6)
print(rectangle1.compute_area())
print(rectangle1.compute_perimeter())
..........................................................................................................
6
 class Animal:
     def speak(self):
         print('animal suond')
class Cat(Animal):
    def speak(self):
        print ('meu')
class Dog(Animal):
    def speak(self):
        print('bark')
cat1=Cat()
dog1=Dog()
cat1.speak()
dog1.speak()
.............................................................................................
7
class shape:
    def area(self):
        return 'it is shape area'
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
class triangla(shape):
    def __init__(self,hight,base):
        self.hight=hight
        self.base=base
    def area(self):
        return 0.5*(self.hight*self.base)
sq1=square(10)
st1=triangla(12,6)
print(sq1.area())
print(st1.area())
........................................................................................
8
class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return self.name+str(self.salary)
 class Maneger(Employee):
    def __init__(self,name,salary,depratment):
        super().__init__(name,salary)
        self.depratment=depratment
m1=Maneger('home_work3.txt',60000,'It')
e1=Employee('home_work3.txt',4000)
print(m1.salary)
......................................................................................
9
class Vehicle:
    def drive(self):
        print("Vehlicle dive")
class bike(Vehicle):
    def drive(self):
        print("bike diver")
class Truck(Vehicle):
    def drive(self):
        print('truck drive')
b1=bike()
t1=Truck()
b1.drive()
t1.Truck()
..............................................................................................................
10
class bird:
    def fly(self):
        print('birt can fly')
class eagle(bird):
    def fly(self):
        print('can not fly')
class penguin(bird):
    def fly(self):
        print('indicate')
ea1=eagle()
pe1=penguin()
ea1.fly()
pe1.fly()
..............................................................................................
amount=int(input("enter the number yuo want to desposit or withdarw"))

class account:
    def __init__(self,balance):
        self._balance=balance
    def despoit(self,amount):
        self._balance+=amount
    def witharw(self,amount):
        if amount<=self.balance:
            self._balance-=amount
        else:
            print("you can't witharw")
    def get_balance(self):
        return self._balance
a1=account(400000)
a1.despoit(amount)
print(a1.get_balance())
.............................................................................................................
12
class book:
    def __init__(self,title,author,page):
        self.__title=title
        self.__author=author
        self.__page=page
    def __str__(self):
        return f""""the title of this book is{self.__title}\n
         and the author of this book is {self.__author}\n
          and the book has{str(self.__page)}page"""
book1=book("serag atwarikn","faiz monammad katib","4500")
print(book1)
.....................................................................................
13
class laptap:
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
    def discoun(self):
        return self.__price(self.__price*0.2)
    def dispaly__laptap_details(self):
        return f"""the brand of this laptap is{self.__brand} the model of this laptap{str(self.__price)}"""

    def discount(self):
        pass


la1=laptap('intall','dell',14500)
print(la1.dispaly__laptap_details())
print('the discount of prie',la1.discount())
.........................................................................................................
14
amount=int(input("enter the number you want to despositor withdarw"))
class bink_account:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def depost(self,amount):
        self.__balance+=amount
    def withraw(self,amount):
        if self.__balance >=amount:
            self.__balance-=amount
        else:
            print("you can't withraw")
    def chack_balantce(self):
        return self.__balance
b1=Bank_accoun('62335',45000)
b1.depost(amount)
print(b1.chack__balance())
................................................................................
15
class student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
    def dispay_details(self):
        print(f"name:{self.name}")
        print(f"Grade:{self.grade}")
        print(f"Age:{self.age}")
student=student("home_work3.txt","A",20)
student.dispay_details()
..........................................................................................
16
list_books=['math','chemstry','hestory','physic']
class library:
    def __init__(self,name,books):
        self.name=name
        self.books=books
    def add_books(self):
        list_books.append('goegrhy')
    def remove_books(self):
        list_books.remove('hestory')
li1=library('my library',list_books)
li1.add_books()
li1.remove_books()
print(li1.books)
.......................................................................
17
list=['home_work3.txt','ahmad','mahammad','khadim','kabie']
class school:
    def __init__(self,name,student):
        self.name=name
        self.student=student
    def add_student(self):
        student-list.append('hussain')
    def remove_student(self):
        'student_list'.remove('mohammad')
school1=school('abdurrahim shahid','student_list')
school1.add_student()
school1.remove_student()
print(school1.student)
....................................................................................
18
team_members=['ailasghar','ailmohammad','bagir','farhd']
class team:
    def __init__(self,name,members):
        self.name=name
        self.members=members
    def add_members(self):
        team_members.append('latif')
    def ream_members.reversed('bagir')
team1=team('unvesity',team_members)
team1.add_members()
team1.remove_members()
print(team1.members)
...............................................................................
19
empolyee_list=['home_work3.txt','ahmad','mohammad','khadim','kabir']
class copmany:
    def __init__(self,name,emolyee):
        self.name=name
        self.emolyee=emolyee
    def add_empolyee(self):
        empolyee_list.append('hussain')
    def remov_emolyee(self):
        empolyee_list.remove('mohammad')
em1=copmany('apple',empolyee_list)
em1.add_empolyee()
em1.remove_empolyee()
print(em1.emolyee)
................................................................................................
20
animale_list:['lion','wolf','fax','dog']
class Zoo:
    def __init__(self,name,animale):
        self.name=name
        self.animale=animale
    def add_animale(self):
        animale_list.append('cat')
    def remove_animove(self):
        animale_list.remove('wolf')
zoo1= Zoo('habul zoo','animale_list')
zoo1.add_animale()
zoo1.remove_animale()
print(zoo1.animale)
.........................................................................
21
class filemanager:
    def __init__(self,filename):
        self.filename=filename
    def wite_to_file(self,content):
        with open(self.filename,'w') as file:
            file.write(content)
            print(f"content written to{self.filename}")
    def read_from_file(self):
        tey:
        with open(self.filename,'r') as file:
            file.write(content)
            print(f"content written{self.filename} ")
                  Contene=file.read
        except fileNotfounderror:
              print(f"the file {self.filename}") dose not exist.(")"
                return None
file-manager=filemanager("example.txt")
file_manager.writ_to_file("ldello this a test.")
content=file-manager.read_from-file()
if content is not none:
    print("content read from file:")
    print(content)
..................................................................

22
from datetime import datetime
class LOP:
    def __init__(self,filename='error_log.txct'):
         self.filename=filename

    def with_error(self,message):
         with open(self.filename, 'a') as file:
            timestamp=datetime.now().
strftime("%Y-%m-%d %H:%M:%S")
         file.write(f"[{timestamp}] ERROR:{message}\n")

 if __name__=="__name__":
     logger=Lop()
     logger.write_error("this is an error message.")

27
class ltem:
    def __init__(self,name, price):
        self.name=name
        self.price=price

class shoppingCart:
    def __init__(self):
        self.items=[]
    def add(self,item):
        self.items.append(item)
    def remove(self,item):
        self.items.remove(item)
    def dispaiy(self):
        for itme in self.items:
            print("name:",item.name, "price:",item.price)
i1=item("bread",20)
i2=item("apple",30)

cart=shoppingCart()
cart.add(i1)
cart.add(i2)
cart.remove(i1)
cart.remove()
29
class preson:
    def __init__(self,flight_number, destination,name):
        self.f=flight_number
        self.d=destination
        self.n=name
class Flight:
    def __init__(self):
        self.passengers=[]
     def add(self,passenger):
        self.passengers.append(passenger)
    def remove(self,passenger):
        self.passengers.remove(passenger)
    def dispaly(self):
        for passenenger in self.passengers:
            print("flight number:",passenenger.f,"","destination:",passenenger.d,"","name:",passenenger.n)
p1=preson(2216,1200,"Mohammad")
p2= preson(2217,500,"Ali")
f1=Flight()
f1.add(p1)
f1.add(p2)
f1.remove(p1)
f1.dispaly()
