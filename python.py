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

slicing a string [start index : end index] # does stops before the end   ## you can also have [4:] from 4th to the end, [:4] from 0 to 4th

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
___________________________________________________________________________________________________________________________________________

#FOR LOOP
numbers = [1, 23, 4, 5, 63, 2]
numbersCube = []
for i in numbers:
    numbersCube.append(i**2)   # prints squeare rooted list
    
    
numbersCube = [i**2 for i in numbers] # shortened syntax
numbersCube = [i**2 for i in numbers if i % 2 == 0]  # only brings out divideable by 2

_________________________________________________________________________________________________________-__________


