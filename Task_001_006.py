A, B, C = 666, 666, 666
print(f"A is {A} with the identificator {id(A)}\nB is {B} with the identificator {id(B)}\nC is {C} with the identificator {id(C)}")

if id(A)==id(B):
    print('The identificators for A and B are the same.')

if id(B)==id(C):
    print('The identificators for A and C are the same.')

if (id(B)==id(C)) and (id(A)==id(B)):
    print('The identificators of A, B and C are the same.')

