import re

text = "(A&~B)|(~A&B) oraz (x&~y)|(~x&x)"
# pattern = r'\((?P<left>[A-Za-z]+)&~(?P<right>[A-Za-z]+)\)|\((?P<left2>[A-Za-z]+)&~(?P<right2>[A-Za-z]+)\)'
pattern = r'\(A&~B\)|\(~A&B\)'
pattern = "(A&~B)|(~A&B)"
# replacement = r'(\g<left>/\g<right>)|(\g<left2>/\g<right2>)'
replacement = "(A/B)"

# result = re.sub(pattern, replacement, text)
result = text.replace(pattern, replacement)
print("Zmodyfikowany tekst:", result)
