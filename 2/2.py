import random
import math
from math import gcd
from sympy import isprime

def generate_keys(key_size=1024):
    """Generate RSA public and private keys"""
    
    # Step 1: Generate two large prime numbers
    p = get_large_prime(key_size // 2)
    q = get_large_prime(key_size // 2)
    while p == q:
        q = get_large_prime(key_size // 2)
    
    # Step 2: Compute n (modulus)
    n = p * q
    
    # Step 3: Compute Euler's totient function
    phi = (p - 1) * (q - 1)
    
    # Step 4: Choose public exponent e
    e = 65537  # Common choice (2^16 + 1)
    while gcd(e, phi) != 1:
        e += 2
    
    # Step 5: Compute private exponent d
    d = modular_inverse(e, phi)
    
    # Public key (e, n), Private key (d, n)
    return (e, n), (d, n)

def get_large_prime(bits):
    """Generate a large prime number"""
    while True:
        num = random.getrandbits(bits)
        # Ensure it's odd and has the right bit length
        num |= (1 << bits - 1) | 1
        if isprime(num):
            return num

def modular_inverse(a, m):
    """Compute modular inverse using Extended Euclidean Algorithm"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def encrypt(message, public_key):
    """Encrypt message using public key"""
    e, n = public_key
    # Convert message to integer
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    # Encrypt
    encrypted_int = pow(message_int, e, n)
    return encrypted_int

def decrypt(encrypted_int, private_key):
    """Decrypt message using private key"""
    d, n = private_key
    # Decrypt
    decrypted_int = pow(encrypted_int, d, n)
    # Convert back to string
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')
    return decrypted_bytes.decode('utf-8')

# Example usage
if __name__ == "__main__":
    # Generate keys (in practice, use larger key sizes like 2048 or 4096 bits)
    public_key, private_key = generate_keys(1024)
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    # Original message
    message = "Hello, RSA Cryptosystem!"
    print(f"\nOriginal Message: {message}")
    
    # Encrypt
    encrypted = encrypt(message, public_key)
    print(f"\nEncrypted Message (as integer): {encrypted}")
    
    # Decrypt
    decrypted = decrypt(encrypted, private_key)
    print(f"\nDecrypted Message: {decrypted}")
    
    # Verification
    print("\nVerification:", "Success!" if message == decrypted else "Failure!")