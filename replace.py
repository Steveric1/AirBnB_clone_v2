#!/usr/bin/python3

# def escape_double_quotes(input_string):
"""This module defines a function to escape double quotes in a string"""
import shlex

s = "quoted_string_with_underscores"
tokens = shlex.split(s)
quote = shlex.quote(s)

for token in shlex.split(s):
    if '_' in token:
        key = token.split('_').replace('_', ' /')
        
print(tokens)
# print(quote)

# def escape_double_quotes(input_string):
#     new_dict = {}
#     for arg in input_string:
#         if '=' in arg:
#             k = arg.split('=', 1)
#             value = k[1]
#             key = k[0]
#             
#             if value[0] == value[-1] == '"':
                
