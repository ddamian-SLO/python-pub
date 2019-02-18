print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Strip White Space Example - Right Side
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Strip White Space Example - Left Side
favorite_language = ' python'
favorite_language = favorite_language.rstrip()

# Using single quote in print 
message = "One of Python's strengths is its diverse community." 
print(message) # This prints fine

# This will will result in a syntax error
# message = 'One of Python's strengths is its diverse community'
# You are basically telling the compiler to end the string at 'One of Python' and then the rest is 
# just plain text.

# Exercise in Crash Course chapter 2 page 29
# 2-3

person_name = "Dave"
print("I'm sorry " + person_name + "... I'm afraid I can't do that...")

# Title Case Examples
# 2-4

print(person_name.upper())
print(person_name.lower())
print(person_name.title())

# 2-6 Concatenation Example
famous_quote = "Ask not what your country can do for you, but what you can do for your country."
famous_author = "John F. Kennedy"

print("Famous Quote - String Concatenation Example")
print(famous_author + " once said, " + '"' + famous_quote + '"')