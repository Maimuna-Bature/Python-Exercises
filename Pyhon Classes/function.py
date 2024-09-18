def say_twice(x):
    print(x)
    print(x)
say_twice(4)

#example2
def add_2_num(x,y):
    print(x+y)
add_2_num(3,4)

#return type
def mult(x,y):
    return x * y
a = mult(4,5)
print(a)

#example4
def even_odd(x):
    num =int(input("enter a number: "))
    if num%2==0:
        return "the number is even"
    else:
        return "the number is odd"
even_odd(5)

#overloading
def greet(name, msg="Hello"):
    print(msg, name)
greet("Alice")
greet("Bob","Hi")

#overriding
class Animal:
    def sound(Self):
        print("the animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("the dog barks")
        
my_dog=Dog()
my_dog.sound()