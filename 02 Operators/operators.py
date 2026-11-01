# Student Marks & Result Calculator
print("===== STUDENT RESULT CALCULATOR =====")

# get student details
name = input("Enter your name: ")

# get subject marks
python = float(input("Enter python marks: "))
sql = float(input("Enter sql marks: "))
html = float(input("Enter html marks: "))
css = float(input("Enter css marks: "))
javascript = float(input("Enter javascript marks: "))

# Arithmetic Operators
total = (python + sql + html + css + javascript)
average = total / 5
percentage = (total / 500) * 100

# Comparition Operators
passed = (
    python >= 35 and
    sql >= 35 and
    html >= 35 and
    css >= 35 and
    javascript >= 35
)

# Logical Operators
if passed and percentage >= 90:
    gread = "A+"
elif passed and percentage >= 75:
    gread = "A"
elif passed and percentage >= 60:
    gread = "B"
elif passed and percentage >= 50:
    gread = "C"
elif passed:
    gread = "D"
else:
    gread = "Fail"
    
# Assignment Operator
bonus = 0
bonus += 5

# Display Result
print("=== STUDENT RESULT ===")
print("Student name: ",name)
print("Total Marks: ",total)
print("Average: ",average)
print("Percentage: ",percentage,"%")
print("Gread: ",gread)

# Membership Operator
subjects = ["PYTHON","SQL","HTML","CSS","JAVASCRIPT"]
print("python included: ","PYTHON" in subjects)

# Identity Operator
result1 = ["Pass"]
result2 = result1

print("Same result objects: ",result1 is result2)

print("=======================")
