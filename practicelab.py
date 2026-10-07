# user = "JFKMMMM"
# print(len(user))

# num_chars = len("santa")

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(alphabet[0],
#       alphabet[1], 
#       alphabet[7], sep="\n")

# word1= "july"
# word2 = "Aug"
# word3 = "Sep"
# statement = word1 + " " + word2 + " " + "The best month is "+ word3
# print(statement)

# print(f"{2**2=}")
# print(f"{3*3+9**3=}")

# Ask the user for their name and age, then print:
# name = input("Enter your name:")
# age = input("Enter your age:")
# print(f"Hello {name}, you are {age} years old")

# number = "jan"
# print(f" {number:s}")

# my_str = "http://reddit.com/r/python"
# print(my_str[10:-5])

# print(f"{'Studio Jan':20} {'Rate':5}")
# print("-" * 30)
# print(f"")

# Ask for a product name, price, and quantity, then pr  int something like: You bought 3 notebooks at $4.50 each.
product_name = input("Enter the product name:")
price= input("Enter the price:")
quantity = input("Enter the Quantity:") 
print(f"You bought {quantity} {product_name} at ${price} each.")

name1 = "apple"
name2 = "orange"
name3 = "mango"

price1 = f"${167.20:.2f}"
price2 = f"${334.21:.2f}"
price3 = f"${57.90:.2f}"

quantity = 31

print(f"{'Product':<30} {'Price':>10} {'Quantity':>5} ")
print("-"*35)
print(f"{name1:<20} {price1:>10} {quantity:>10}")
print(f"{name2:<20} {price2:>10} {quantity:>10}")
print(f"{name3:<20} {price3:>10} {quantity:>10}")
