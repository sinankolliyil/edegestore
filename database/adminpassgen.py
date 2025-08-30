from passlib.hash import sha256_crypt

# Generate hash for your password
password = "admin@123"
hash = sha256_crypt.hash(password)

print(hash)