a = 7
b = 'hello'
c = 13.4
print(f"parameter a = {a}\nparameter b = {b}\nparameter c = {c}\n")
print(f"parameter a data type and identificator are:\n {type(a)}\n {id(a)}\nparameter b data type and identificator are:\n {type(b)}\n {id(b)}\nparameter c data type and identificator are:\n {type(c)}\n {id(c)}")

a = 'hello'
print(f"parameter a is now = {a}\nparameter b is now = {b}\n")
print(f"parameter a data identificator is:\n {id(a)}\nparameter b identificator is:\n {id(b)}")

if id(a)==id(b):
    print('The identificators for a and b are now the same.')
else:
    if id(a)==id(c):
        print('The identificators for a and c are now the same.')
    else:
        print('The identificators of a, b and c are still different.')