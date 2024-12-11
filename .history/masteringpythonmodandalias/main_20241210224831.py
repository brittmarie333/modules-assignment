# main.py
# Import text_utils using an alias and utilize its functions

import text_utils as tu

statement = "I can't believe that I'm almost done with Python!"

reversed_str = tu.reverse_string(statement)
print(reversed_str, "\nStatements in reverse always look wierd!")

capitalized_str = tu.capitalize_string