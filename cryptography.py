from cryptography.fernet import Fernet

key = Fernet.generate_key()
# Save the generated key
key
f = Fernet(key)
message = b'Secrets go here'

encrypted = f.encrypt(message)
encrypted

#You can decrypt the data using a Fernet object created with the same key:
f = Fernet(key)
f.decrypt(key)
