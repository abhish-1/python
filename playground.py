#input by default is string in py, gotta typecaste them.
name = input("please enter your name ")
print("my name is",name)
a =float(input())
b =int(input())
sum = a+b
#formatting ->
print("sum of {} and {} is {}".format(a,b,sum))
print("sum of {0} and {1} is {2}".format(a,b,sum))  #index based formatting
print("sum of {a} and {b} is {sum}".format(a=5,b=10,sum=15))  #value based formatting
#we dont use both of these we use F-STRING.
print(f"sum of {a} and {b} is {a+b}")

#range function
for i in range(1,11,1):
    print (i)

#function
def func():
    print("Hello")

func()

#lambda function for high order function.(Not used much)
lambda a,b: a+b

#STRINGS IN PYTHON are immutable.
len(str) 
str[0:3] #SLICING -> the end is not included, there is another method by taking negative indices

#List
list = [66,84,7,"hi"] # slicing works the same way
for i in list:
    print(i)
list.append(val)
list.insert(idx,val)
list.sort()
list.reverse()

#tuple, same but yep tuple is immutable whereas list is mutable
tup = {11,22,33}
tuple.index(val) #returns teh first occurence
tuple.count(val) #returns total occurence

#Dictionary -> Unique (key)-value pair
info = {
    "name": "abhishek",
    "cgpa":8.57,
    "crush": "gettfoutahere"
}
info["crush"]
info.keys() #return all keys
info.values() #return all values
info.items() #return Key-values pairs
info.get(val) #return val acc to key
info.update(new_item) #adds new item to dict

#Sets
set = {1,2,3,22,3,22}
set.add(val)
set.remove(val)
set.clear()
set.pop() #removes a random variable
set.union(set2)
set.intersection(set2)

#OOP
class Student:
    name = "atul"
    def _init_(self,name): #name ko define mhi kia h, instance attribute gets higher priority as compared to class attribute
    #instance method me pehle element self hota h    
        print("constructor")
        self.name=name

stu1 = Student("Abhi") #python me constructor overload nhi kam krta h last wala ko manega agr multiple init class h to.

class Laptop:
    storage_type = "ssd"
    def _init_(self,RAM, storage):
        self.RAM=RAM
        self.storage=storage

        @classmethod   ##static method decorator
        def get_storage_type(cls):
        #class methods me hmesa cls lgta h
            print(f"storage type = {cls.storage_type} {cls.RAM}")

        def get_info(self): #instance method
            print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

        @staticmethod   #static method
        def calc_discount(price, discount):
            final_price=price-(discount*price/100)
            print(f"discount price = {final_price}")

#function overload -> Eg '+' can concatanate as well as add nos in python i.e that operator is overloaded
#function overriding (Inheritance)
#duck typing -> nothing spl.  2 diff classes me agr ek sa hi kam krne wala function h to uska nam same rkhdo

#FILE OPERATIONS.
f = open("path-absolute","r"/"w")
data = f.read() #data m sb store ho gya h
data = f.readline() #just ek line ab what 's cool is agr ek bar or readline lgao to agli line read ho jaegi
data = f.readline() #reads the second line
# assume reading writing in file as a pointer concepts like there is a pointer that sees all these operations
print(data)

f.write("hey nig sup ?") #this will erase all the data and then write.
f.close()  #always close file 

# r -> reading (default)
# w -> write (after truncating the existing material) and it can create as well if the file dne
# a -> append to the end ... (pointer is at end) 
# x -> create a new file and write
# + -> multiple modes k lie 
# r+ means read bhi n write b, w+ me write and read v, a+ me write b read bhi, now the diff is of pointer position ab r+ me ptr is at the
#start so if you do a write operation to jitna tm add kro n words utna part of prev written in the start wo truncate hoke write hoga.
# similar goes for the rest.
# b -> for binary mode (audio video are not text tehy are binary actually)
# t -> text mode by default (r k mtlb r+t)
# ab y pointer wala concept yad rkhna 

#with keyword -> explicitly no need to call teh close()
with open("file.txt", "r") as f:

# OS module in python helps in doing operation related to OS like file mgmt.
import os
os.remove("path")

#ShortCaps ->
#you need to search a word from a string then [if("pyhton" in data)]

#ERROR HANDLING
#try: except: else: finally

#LiST COMPREHENSION
sq = [i*i for i in range(6) if i%2!=0] #sq = [1,9,25]

#JSON MODULE

import json

json.dumps() #s is for string, py data gets converted to json data
json.loads() #json data gets converted into python data

json.load(data, f ) # file formats me y dono, json se read, f is the file you opened
json.dump(data, f, indent = 4, sort_keys=True) # json me write krna h to dump

json_str = '{"name": "Abhsiehk, "height":178, "address":{"city":"Gaya", "state":"bihar"}}'
py_form = json.loads(json_str)










        
