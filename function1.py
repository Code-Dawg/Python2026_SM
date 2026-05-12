def calculate_mark(marks):
    if(marks > 100 or marks <0):
        print("Invalid")
    elif(marks>=90):
        return "A"
    elif(marks>=80):
        return "B"
    elif(marks>=70):
        return "C"
    elif(marks>=60):
        return "D"
    else:
        return "E"
    


def check():
    while True:
            a=int(input("Enter the number:"))
            if 0<a<100:
             return a
            
            else:
                print("invalid Number,Enter again")
    

num_1=check()
num_2=calculate_mark(num_1)
print(num_2)




    
     

