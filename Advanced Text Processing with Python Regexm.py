import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key = "Occupation"

# Regex pattern to match 'Key: Value'
pattern = rf"{key}: ([^;]+)"

# Find the value corresponding to the key
match = re.search(pattern, text)

if match:
    value = match.group(1)
    print(f"The value for '{key}' is: {value}")
else:
    print(f"Key '{key}' not found in the text.")
