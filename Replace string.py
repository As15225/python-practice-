# Replacing string in python used with str.replace

# str="Python Python Python i avoid but Python likes me i can't Avoid"
# print(str.replace("Python", "Katrina"))
# print(str.replace("Python", "katrina", 3))

# split string is used with str.split

str="My name is asispal singh"
print(str.split())
str2=['My', 'name', 'is', 'asispal', 'singh']
print(":".join(str2))
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())
print(str.capitalize())

str3= "You dont have any public repositories yet"

print(str3.rstrip())
print(str3.lstrip())
print(str3.strip())


print(str3.startswith("You"))
print(str3.endswith("yet"))


print(str3.isalnum())
print(str3.isalpha())
print(str3.isdigit())
print(str3.islower())
print(str3.isupper())
print(str3.istitle())
print(str3.isspace())

str4= "A standard short paragraph is a concise, self-contained unit of writing generally consisting of 3 to 6 sentences. It includes a topic sentence that introduces the main idea, supporting sentences that provide details or evidence, and a concluding sentence that summarizes the core message"

print(len(str4))
print(str4.find("sentences"))
print(str4.index("short"))
print(str4.rfind("sentences"))
print(str4.rindex("short"))











