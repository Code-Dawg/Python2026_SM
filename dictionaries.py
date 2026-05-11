student={
    "name":input("Enter the name:"),
    "class":int(input("Enter the class:")),
    "Course":input("enter the course:"),
    "Marks1":int(input("Enther the marks in maths:")),
    "Marks2":int(input("Enther the marks in science:")),
    "Marks3":int(input("Enther the marks in english:"))

}
print(student)
Marks=(student["Marks1"]+student["Marks2"]+student["Marks3"])/3
print(Marks)