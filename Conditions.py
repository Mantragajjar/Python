name = input("Enter your name: ")

if len(name)<3 :
    print("Entered name must be atleast 3 character.")
elif len(name)>50:
    print("Entered name must be a maximum of 50 characters.")
else :
    print("Entered name looks good")