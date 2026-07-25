#Single-quoted string 
a = 'Hello, Python!' 
#Double-quoted string 
b = "Hello, World!" 
#Triple-quoted string (useful for multi-line strings) 
c = '''This is a multi-line string.'''

#--------------------------------------------------------------------------------------------
# Sting slicing
text ="Hello, Python!"
print(text[0:8]) #The o/p will befrom H to P,

# String slicing prints the range of index that u provide
#-----------------------------------------------------------------------------------------

# Step parimeters

print(text[::2]) # o/p will be Hlo yhn
# This will print every second character, o/p will be Hlo yhn

#----------------------------------------------------------------------------------
# String Formating

name ="John" 
age =25 # Using format() 
print("My name is {} and I am {} years old.".format(name, age))
# Using f-strings (Python 3.6+) 
print(f"My name is {name} and I am {age} years old.") 
#O/p will be same
