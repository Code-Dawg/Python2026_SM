# Write a function sum_natural(n) that returns the sum of the first n natural numbers using a loop.
def sum_natural():
    sum=(n*(n+1))/2
    return sum
n=int(input("Enter a number:"))
sum_ofnumber=sum_natural()
print(f"Sum of First Natural no is:{sum_ofnumber}")