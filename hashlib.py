import hashlib

secret = "Secrets go here"
bsecret = secret.encode()

m = hashlib.md5(bsecret)
m.update(bsecret)