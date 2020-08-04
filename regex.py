import re

cc_list = 'File Here abcd@gmail.com'

# searching
re.search(r'File', cc_list)

#character sets
re.search(r'[F,G]il[e,i]', cc_list)
re.search(r'Fi[a-z][a-z]', cc_list)
re.search(r'[A-Za-z]+', cc_list)

# character classes
re.search(r'\w+', cc_list)

# Groups
match = re.search(r'(\w+)\@(\w+)\.(\w+)', cc_list)
match.group(0)

# named groups
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(f'''name: {matched.group("name")}
Secondary Level Domain: {matched.group("SLD")}
Top Level Domain: {matched.group("TLD")}''')

# Find all
matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
names = [x[0] for x in matched]
print(names)

# Find iterator
match2 = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
for m in match2:
    print(m.groupdict())

# substitution
re.sub("\d", "#", "The passcode you entered was 09876")
users = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)","\g<TLD>.\g<SLD>.\g<name>", cc_list)

#compiling
regex = re.compile(r'\w+\@\w+\.\w+')