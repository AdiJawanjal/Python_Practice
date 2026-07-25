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

text = "Welcome to Python!" 
print(text[:7]) # Output: Welcome 
print(text[-7:]) # Output: Python!

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
#----------------------------------------------------------------------------------

text ="apple,banana,orange" 
print(len(text))
fruits = text.split(",") 
print(len(fruits))
print(fruits)
new_text =" - ".join(fruits) 
print(new_text)

#-------------------------------------------------------------------

pi =3.14159265 
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# O/P = 3.14
#---------------------------------------------------------------------

# Alignment

text ="Python" 
print(f"{text:>10}")# Right align 
print(text)
print(f"{text:<10}") # Left align 
print(f"{text:^10}") # Center align

# it just add spaces like if right align then it will add sapce on the left side like this "    Python" and for center "  Python  "
#-------------------------------------------------------------------


