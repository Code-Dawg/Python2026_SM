# Write a program to:
# Create a new list containing only even numbers
# Create another list containing only numbers greater than 10
# Print both lists
numbers = [12, 7, 19, 3, 8, 15, 4, 22]
num1=[]
num2=[]
num1=[x for x in numbers if x%2==0] 
print(num1)
num2=[x for x in numbers if x>10]
print(num2)
