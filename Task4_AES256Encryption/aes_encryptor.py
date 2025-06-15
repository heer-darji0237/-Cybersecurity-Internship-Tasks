from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Key generated and saved to 'secret.key'")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"✅ Encrypted file saved as: {filename}.enc")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    output = filename.replace(".enc", ".dec")
    with open(output, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"✅ Decrypted file saved as: {output}")

if __name__ == "__main__":
    print("\n🔐 AES-256 File Encryption Tool")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        file = input("Enter filename to encrypt: ")
        encrypt_file(file)
    elif choice == "3":
        file = input("Enter .enc filename to decrypt: ")
        decrypt_file(file)
    else:
        print("❌ Invalid choice.")
