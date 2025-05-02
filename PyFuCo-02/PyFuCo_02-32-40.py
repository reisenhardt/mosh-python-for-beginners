def greet_user(first_name="Sven", last_name="Lensman"):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


def calc_cost(total, shipping, discount):
    print(f" {total}, {shipping} , {discount}")


print("Start")
greet_user("Smith", "Mary") # Positional arguments help to change the Sequence
calc_cost(total=50, shipping=5, discount=0.1) # Keyword arguments make the code more readable
print("Finish")

