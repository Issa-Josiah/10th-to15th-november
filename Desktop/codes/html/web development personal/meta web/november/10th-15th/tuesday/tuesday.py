"""
variables

-container that hold something
linked to a memory


====rules of namign====

name according to what it represent
do not use inbuilt keywords like if ets
dont start with a number or a special character
choose camel case (Lastname)or snakecase(Last_name)
"""


# print statements

first_name="Issa" ;
second_name="Josiah";

# input tag

last_name=input("enter your last name: ");

print(first_name, end=" ");
print(second_name);
print(first_name, second_name, last_name);
print(first_name + last_name);


'''
functions
-does something
-group related procedures into one "call"

=========rules=========
-must have def keyword
-must have a function name
-must have a paranthesis and a colon
-must do only one thing
-everything inside must have an indentation of 4 spaces . press tab to archieve this
'''

# plane function
def salamu():
    print("Hello Ninja")
    
# calling a function
salamu()
    
# parametarized function
def greetguest(name):
    print("hello", name)
    

