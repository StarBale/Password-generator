import random
import string

# define the length of the password
length = int(input("Enter the length of password: "))

# define the set of characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# generate a random password using the set of characters
password = ''.join(random.choice(characters) for i in range(length))

# print the generated password
print("Your password is: ", password)
