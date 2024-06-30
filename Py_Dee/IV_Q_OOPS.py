'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Inheritance(Single,Multiple,Multilevel,Hierchical,Hybdrid)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

## 1......... ## Single Inheritance
#Parent Class
class Brand:
    def __init__(self, name):
         self.name = name
    
    def item(self):
        pass
# Child Class
class Catagory(Brand):
    def item(self):
        return "Shirt"

catg = Catagory("Polo")
print (catg.name)
print (catg.item())

## 2......... ## Multiple Inheritance
#Parent Class 1
class Lux:
    def __init__(self, name):
        self.name =name
    def show_lux_item(self):
        return self.name
#Parent Class 2
class Price:
    def __init__(self, price_tag):
        self.price_tag = price_tag
    
    def show_price_tag(self):
        return self.price_tag
# Child Class
class Store(Lux, Price):
    def __init__(self, name, price_tag):
        Lux.__init__(self, name)
        Price.__init__(self, price_tag)

store = Store("RedDOt", 4999)
print(store.show_lux_item())
print(store.show_price_tag())

## 3......... ## Multilevel Inheritance
#GrandParent Class (Base Class)
class Shirt:
    def __init__(self, name):
        self.name = name

    def show_shirtname(self):
        return self.name
#Parant Class
class Types(Shirt):
    def t_shirt(self):
        return("Red")
#Child Class
class Color(Types):
    def red(self):
        return("Blood Red")

colour = Color("Full Length")
print(colour.show_shirtname())
print(colour.t_shirt())
print(colour.red())


## 4......... ## Herarchcal Inheritance
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

# Child Class 1
class Dog(Animal):
    def sound(self):
        return "Bark!"

# Child Class 2
class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Mittens")
print(dog.name, "Work is while see the people", dog.sound())  
#print(dog.sound())  
print(cat.name) 
print(cat.sound())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Accesser Mothos (Public,Private,Protect)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

