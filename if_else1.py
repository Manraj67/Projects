""""Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And 
further, bikes and cars are divided into 2 subcategories. To give the user better selection options."""
print("1. bike,")
print("2. car")
a=int(input("Which one do you choose. "))
if a==1:
    print("1. scooter")
    print("2. motorcycle")
    b=int(input("Which one do you choose"))
    if b==1:
        print("You have chosen scooter")
    else:
        print("You have chosen motorcycle")
else:
    print("1. SUV")
    print("2. Sedan")
    c=int(input("Which one do you choose"))
    if c==1:
        print("You have chosen SUV")
    else:
        print("You have chosen Sedan")