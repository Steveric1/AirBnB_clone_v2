#!/usr/bin/python3

# def escape_double_quotes(input_string):
#     escaped_string = ""
#     for char in input_string:
#         if char == '"':
#             escaped_string += r'\"'  # Escape double quotes with a backslash
#         else:
#             escaped_string += char
#     return escaped_string
# 
# # Example usage:
# input_string = 'This is a "quoted" string'
# escaped_string = escape_double_quotes(input_string)
# print(escaped_string)

dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

new_dict = {}
for key, value in dictionary.items():
    value = str(value)  # Convert value to string
    value = value.replace('"', r'\"')  # Replace double quotes
    new_dict[key] = value
    
print(new_dict)

