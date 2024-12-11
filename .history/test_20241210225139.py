def reverse_string(s, str):
# function to reverse a string
    return s[::-1]

def capitalize_string(s: str):
# function to capitalize a string
    return s.upper()


import text_utils as tu

statement = "i can't believe that I'm almost done with Python!"

reversed_str = tu.reverse_string(statement)
print(reversed_str, "\nStatements in reverse always look wierd!")

capitalized_str = tu.capitalize_string(statement)
print("I fixed your statement: ", capitalized_str)