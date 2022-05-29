BASIC MATH OPERATORS :
7 / 3 (2.3333)
7 // 3  (2) rounds down
7 % 3 (1) returns whats left after division
2**2  (4) squared
_  to use the last sum


x = ("apple", "banana", "cherry")  tuple
x = ["apple", "banana", "cherry"] list
x = {"name" : "John", "age" : 36} dict
type()  #to check for type

"mr gregs house \n is there" # second part goes to other line    

\t # is tab in a string

len() #returns the length of the string

.index() # returns the index of what you are lookign for

.count()  # how many times it appears

.slice(start index, stop index, step) # does stops before the end   ## you can also have [4:] from 4th to the end, [:4] from 0 to 4th

'string you want to check' in variableName  #check if a variable is in a string  ## can also use   not in

.upper() #to upper case a string .lower()

print(f"the sum of {x} and {y} is {sum}")  # f formating , like ${} in javascript

list.append(content)  # adding something to the back of a list
list.insert(index, content) #inserting to a list
list.extend(list) # addign 2 lists together
list.pop(content) # removes and returns popped item, leave it empty to get the last element
list.clear() #clear a list
list.count(content)  # returns the number of times a value appears in a list
list.sort()  # sort your list
list.reverse() # reverses the elments in a list

age [13,11,12,34,67,85]
list.sort(reverse=True)
#comes out larger to smaller sorted


ages (12, 34, 56, 67) #ordered, unchangeable, 

pass - do nothing
___________________________________________________________________________________________________________________________________________

#FOR LOOP
numbers = [1, 23, 4, 5, 63, 2]
numbersCube = []
for i in numbers:
    numbersCube.append(i**2)   # prints squeare rooted list
    
    
numbersCube = [i**2 for i in numbers] # shortened syntax
numbersCube = [i**2 for i in numbers if i % 2 == 0]  # only brings out divideable by 2

pass # to put loop on pause , not to execute

_________________________________________________________________________________________________________-__________

#IN LOOP

numbers = [1, 23, 4, 5, 63, 2]
print(23 in numbers) # returns true
______________________________________________________________________________________________________________________
#SETS
set.update(set2)   # to add 2 sets together


fruits = {'bananas', 'beet', 'carrots'}
fruits.remove('bananas')
print(fruits) # removes bananas, returns an error if the item does not exist,
.discard() # same as remove, but doesnt return an error
.pop() # removes the last element

set1.intersection(set2) # brings out items that are in both sets
set1.symmetric_difference(set2) # brings out items that are not in both lists
set1.difference(set2) # set1 - intersection(set1, set2)
set1.isdisjoint(set2) # check if 2 have common elements

_______________________________________________________________________________________________________

#DICTIONARY
# stored in key:value pair

______________________________________________________________
#CLASS 14.05.2022

phone_book = {
    'john': 57464748,
    'doe': 4555746464,
    'jane': 297632947,
}
# accessing items of a dict
print(phone_book['john'])
# second value is returned if the second value does not exist
print(phone_book.get('does', 'no value'))


# all keys in dict => .keys()
print(phone_book.keys())

# all values => .values()
print(phone_book.values())

# all items => .items()
print(phone_book.items())

# changing a key value
phone_book['jane'] = 777777
print(phone_book)

# update, if the key does not exist, it adds it
phone_book.update({'jane': 64367846})

# check if a key exists
print('john' in phone_book)
print(phone_book)


# removing items
    #pop() method
phone_book.pop('john')
print(phone_book)

    #popitem() removes the last inserted item
phone_book.popitem()


# looping for

for x in phone_book:
    print(f"{x} number is {phone_book[x]}")

# only looping through values
for x in phone_book.values():
    print(x)


# remove all duplicate words in a string
word = " python is a great language c is also a great language"
word_split = word.split(" ")
#set
set_word = set(word_split)
new_word = ' '.join(set_word)
print(new_word)

#dict
new_dict = dict.fromkeys(word_split)
new_word = ' '.join(new_dict)

# counter look pyhton docs
c = Counter(word_split)
new_word = ' '.join(ckeys())
print(new_word)

# WHILE conditional statement, break = stops current execution and the loop
i = 1
while i < 20:
    print(f"{i} : {i ** 2}")
    if i == 9:
        break
    i += 2
______________________________________________________________________________________________________________
#CLASS 15.05.2022

# FUNCTIONS
def <<function_name>> (argument):
    statements
    
    
def area_of_rectangle (length=5, breadth=10):   # uses default parameters if nothing new is passed in
    print(f"length is {length}, breadth is {breadth} and are is {length * breadth}")

# ARGS

def sum_in_numbers (*args):     # takes in any number of arguments
    sum = 0
    for val in args:
        sum += val
    return sum

# KWARGS

def ingredient_for_omlette (**kwargs):
    for key, val in kwargs.items():
        print(f"added {val}: {key}")

ingredient_for_omlette(eggs = 4, carrots = 2, cheese = 3, onions = 1)


# area of 4 sided shapes
# square = l*l
# rectangle = L*b
# after argument you can put type :typeOfValue
def area_of_square(len):
    return len ** 2

def area_of_rectangle(len , br):
    return len * br

def area_of_quadrilateral (length:float = 10, breadth:float = 10):
    if length == breadth:
        return area_of_square(length)
    else:
        return area_of_rectangle(length, breadth)

print(area_of_quadrilateral(5, 7))


'''
 MODULES
    *.py extension
    import                     # importing code from another file, afetr importing you can use it freely
    
import module_name
import module_name as new_name #import numpy as np
from <<module>> import <<function/class>>
from <<module>> import . #import all

from math import sqrt , factorial


'''

_____________________________________________________________________________________________________________________________________

#CLASS 21.05.2022

#OBJECT ORIENTED PROGRAMMING

'''
a class is a blueprint/template for creating objects
    - specify atributes (default values)
    - specify the behaviour
    
CAR = class
-min of 2 doors, max of 4
-4 wheels
- 2 front , 2 back lights

classes have a contructor: special method  __init__

'''

class Car:
    NAME = None  #class variable
    doors = 0  #class variable
    
    def __init__(self, name_of_car:str, no_of_doors:int):
        self.NAME = NAME_OF_CAR
 

#getters and setters, class ( privacy levels in a class)

________________________________________________________________________________________________________________________________

#CLASS 22.05.2022


file handling
create, read, update, delete

open() function
-parameters - filename an the mode
 r => read, open a file for reading
 a => append, open a file for appending
 w => write, open a file for writing, overwrites the file
 x => create, create a file 
 t => text mode(default)
 b => binary mode
 
 
 methods:
 - read(): returns the whole content of a file by default
 - read(number): reads the number of files specified
 - readline()
 - write() : writes to a file
 
 
 
'''
f_write = open ("text1.txt", 'w')
f_write.write("its a wonderful day")
f_write.close()

f_append = open("text1.txt", "a")
f_append.write("\nthe sun is shining and the...")
f_append.close()

f = open("text1.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line.rstrip('\n'))

if os.path.exists("text.xlsx"):
    os.remove("fileName") #deletes the file



__________________________________________________________________________________________________________________________________________
29.05.2022

 #IMPORTING FROM MODULE, PACKAGES
  
 from <<fiel name>> import <<what you want to import (* => to import all)>> 




