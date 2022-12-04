print ("Hello, World")

# %%
# Ask user for their name
name = input("What is your name?")
print ("hello, ")
print(name)
# Works, but not the most efficient way to write this code

# %%
name = input("What is your name?")
print("Hello, " + name) # More efficient than before

# %%
# format string
print(f"hello, {name}")

# %%
# String Functions

# Remove whitespace from string
name = input("What is your name?")
name = name.strip()
