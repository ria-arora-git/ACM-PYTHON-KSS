#QUESTION 1

m= int(input("Enter the starting number : "))
n = int(input("Enter the ending number : "))
sum=0

for i in range(m,n+1):
    sum=sum+i

print(f"The sum of numbers from {m} to {n} is {sum}")

#QUESTION 2
x = int(input("Enter the first number : "))
y = int(input("Enter the last number : "))

if x%y==0:
    print(f"{y} perfectly divides {x}")
elif y%x==0:
    print(f"{x} perfectly divides {y}")
else:
    print("Not a perfect division")


#QUESTION 3
diameter = int(input("Enter the diameter of the circle : "))
pi=3.14

area=pi*((diameter/2)**2)
perimeter=pi*diameter

print(f"The area of the circle is {area} and the perimeter is {perimeter}")


#QUESTION 4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter the number : "))

print(f"The factorial of {number} is {factorial(number)}")


#QUESTION 5
n = int(input("Enter the number of lines you want for the pattern : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()