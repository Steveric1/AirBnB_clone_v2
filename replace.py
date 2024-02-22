#!/usr/bin/python3

# def escape_double_quotes(input_string):
"""This module defines a function to escape double quotes in a string"""


def escape_double_quotes(input_string):
    esc_string = ""
    for char in input_string:
        if char == '"':
            esc_string += r'\"'
        else:
            esc_string += char
    return esc_string
