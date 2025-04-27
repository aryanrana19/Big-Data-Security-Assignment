secret_key = 123

# Encrypt function
def encrypt(number):
    return number + secret_key

# Decrypt function
def decrypt(encrypted_number):
    return encrypted_number - secret_key

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Encrypt the numbers
    enc1 = encrypt(num1)
    enc2 = encrypt(num2)
    
    # Sum the encrypted numbers
    encrypted_sum = enc1 + enc2
    
    # Decrypt the sum
    decrypted_sum = encrypted_sum - (2 * secret_key)
    
    print(f"Encrypted numbers: {enc1} and {enc2}")
    print(f"Encrypted sum (without decrypting first): {encrypted_sum}")
    print(f"Decrypted sum: {decrypted_sum}")

if _name_ == "_main_":
    main()