# %%
print ("Hello, World")

# %%
# Ask user for their name
name = input("What is your name?")
print ("hello, ")
print(name)
# Works, but not the most efficient way to write this code

# %%
print("Hello, " + name) # More efficient than before

# %%
# format string
print(f"hello, {name}")

# %%
# String Functions

# All on same line, neater
name = input("What is your name?").strip().title()

# Remove whitespace from string
name = name.strip()
# Captialise user's name
name = name.capitalize()
# Title based captialisation
name = name.title()

#remove whitespace from str and captialise user's name
name = name.strip().title()

print(f"Hello, {name}")

# %%
name = input("What is your name?").strip().title()
# Split user's name into first and last name
first, last = name.split(" ")
print(f"Hello, {first}")

# %%
# Calculator.py
x = int(input("What's x? ")) # Can nest a function within another
y = int(input("What's y? "))

# z = (y) + (x)

print (x + y)


