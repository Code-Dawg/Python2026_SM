# Write a Python program that takes an integer input from the user and checks whether the number is positive, negative, or zero. Also print if the number is even or odd.
a=int(input("Enter a number:"))
if a>0:
    print(f"The Given NUmber {a} Is Positive ")
elif a<0:
    print(f"The Given NUmber {a} Is Negative ")
else:
    print(f"The Given NUmber {a} Is  Zero ")

if a%2==0:
    print(f"The Given Number {a} is Even")
else:
     print(f"The Given Number {a} is Odd")