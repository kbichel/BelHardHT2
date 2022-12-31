A = input('Please enter an int number: ')
B = input('Please enter a word or letters: ')
C = input('Please enter some value: ')

print(f"value A is {A}, data type is {type(A)}, identificator is {id(A)}")
print(f"value B is {B}, data type is {type(B)}, identificator is {id(B)}")
print(f"value A is {C}, data type is {type(C)}, identificator is {id(C)}")

A = int(input('Please enter an int number again: '))
B = str(input('Please enter a word or letters again: '))
C = float(input('Please enter some value again: '))

print(f"value A is {A}, data type is now {type(A)}, identificator is {id(A)}")
print(f"value B is {B}, data type is now {type(B)}, identificator is {id(B)}")
print(f"value A is {C}, data type is now {type(C)}, identificator is {id(C)}")