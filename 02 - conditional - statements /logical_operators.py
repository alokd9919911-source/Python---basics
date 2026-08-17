age = int(input("Enter your age: "))
has_id = input("Do you have an ID? yes/no: ")

if age >= 18 and has_id == "yes":
    print("Entry allowed")
else:
    print("Entry not allowed")


marks = int(input("Enter your marks: "))

if marks >= 40 or marks == 0:
    print("Condition matched")
else:
    print("Condition not matched")
