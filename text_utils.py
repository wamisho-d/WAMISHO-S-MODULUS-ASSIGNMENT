def reverse_string(s):
 """function to reverse a string."""
 return s[::-1]
def capitalize_string(s):
 """function to capitalize a string."""
 return s.capitalize()

# main.py
import text_utils as tu
reversed_str = tu.reverse_string("hello")
print(f"Reversed string: {reversed_str}")
capitalized_str = tu.capitalize_string("hello")
print(f"Capitalized string: {capitalized_str}")
