import re

file = open(("C:/Users/chris/python/emails.txt"))
file = file.read()
emailnames = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(emailnames)