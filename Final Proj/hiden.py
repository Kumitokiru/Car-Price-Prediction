with open('predictor.py', 'r') as file:
    content = file.read()

# Print the contents of the file with hidden characters (like \r) displayed
print(repr(content))