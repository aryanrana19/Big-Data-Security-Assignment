import random

secret_key = random.randint(1000, 9999)

# Encryption function
def encrypt(value):
    return value + secret_key

# Decryption function
def decrypt(value):
    return value - secret_key

def compute_tax_on_encrypted(encrypted_salary):
    # 10% tax => (salary * 0.1)
    return encrypted_salary * 0.1

# Simulate
salary = 50000
print(f"Original Salary: {salary}")


encrypted_salary = encrypt(salary)
print(f"Encrypted Salary: {encrypted_salary}")

encrypted_tax = compute_tax_on_encrypted(encrypted_salary)
print(f"Encrypted Tax Amount: {encrypted_tax}")

decrypted_tax = decrypt(encrypted_tax)
print(f"Decrypted Tax Amount: {decrypted_tax}")