age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? yes/no: ")

if age >= 18:
    if citizen == "yes":
        print("You can vote")
    else:
        print("You must be an Indian citizen to vote")
else:
    print("You are under 18")
