k=[]

for i in range (1,4):
    number = int(input(f'Please enter number {i}: '))
    k.append(number)
print(k)
k.sort()
print(k)

if k[0]<=1 and k[0]%2!=0:
    print("The smallest number does not meet the requirements as it is less than or equal to 1 and odd")
if k[2]<=((k[1]+k[0])/2) or (k[2]>=k[1]*k[0]):
    print("The largest number does not meet the requirements of being greater than average of the mean and smallest numbers or being less than their product")
if k[1]%3!=0 and k[1]%2!=0:
    print('The mean number is not divisible by 3 and is not even')