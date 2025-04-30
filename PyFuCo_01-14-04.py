name =  "hallo"
print("Enter your name (at least 3 characters): ")
input(name)


if len(name) < 3:
    print(name)
    print("Please enter longer name with at least 3 characters!")
elif len(name) > 10:
    print("Please enter shorter name with max. 50 characters!")
# else:
 #    print("Keine Ahnung!")

