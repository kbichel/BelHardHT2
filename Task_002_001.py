for i in range (0,3):
    a = float(input('Please enter the first length: '))
    b = float(input('Please enter the second length: '))
    c = float(input('Please enter the third length: '))

    if (a+b<=c) or (b+c<=a) or (c+a<=b):
        print(f'The lengths {a}, {b} and {c} can not form a triangle.')
    else:
        print(f'The lengths {a}, {b} and {c} can form a triangle.')
        if a==b and b==c and a==c:
            print((f'The triangle abc is equilateral.'))
        else:
            if a==b or b==c or a==c:
                print(f'The triangle abc is isosceles.')
            else:
                print(f'The triangle abc is scalene.')

print("You have used all your attempts. Please start over.")