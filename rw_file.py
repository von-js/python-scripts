# readlines
file_path = 'path'
with open(file_path, 'r') as open_file:
    text = open_file.readlines()
# direnv write file
text = '''export STAGE=PROD
export TABLE_ID=token-storage-1234'''

with open('.envrc', 'w') as opened_file:
    opened_file.write(text)

# pathlib
import pathlib
path = pathlib.Path("/Users/path/check_pending.py")
path.read_text()
path.write_text("LOG:DEBUG")

# json
import json
with open('service-policy.json', 'r') as opened_file:
    policy = json.load(opened_file)
print (policy)

from pprint import pprint
pprint(policy)
# changing text in file 
policy['Statement']['Resource'] = 'S3'

# dumping file
with open('service-policy.json', 'w') as opened_file:
    poli = json.dump(poli, opened_file)

# YAML
import yaml
with open('verify-apache.yml', 'r') as opened_file:
    verify_apache = yaml.safe_load(opened_file)
pprint(verify_apache)

# dump
with open('verify-apache.yml', 'w') as opened_file:
    yaml.dump(verify_apache, opened_file)