import hashlib
import os
import json

def generate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def save_hashes(directory, output_file):
    hash_dict = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            file_hash = generate_hash(path)
            if file_hash:
                hash_dict[path] = file_hash

    with open(output_file, 'w') as f:
        json.dump(hash_dict, f, indent=4)

def compare_hashes(directory, saved_hash_file):
    with open(saved_hash_file, 'r') as f:
        old_hashes = json.load(f)

    modified = []
    for path, old_hash in old_hashes.items():
        new_hash = generate_hash(path)
        if new_hash != old_hash:
            modified.append(path)

    if modified:
        print("\n⚠️ Modified or tampered files:")
        for file in modified:
            print(f"- {file}")
    else:
        print("\n✅ No changes detected. All files are intact.")

if __name__ == "__main__":
    print("1. Generate and Save Hashes")
    print("2. Check for File Changes")
    choice = input("Choose option (1/2): ")
    directory = input("Enter the directory path: ")
    hash_file = "file_hashes.json"

    if choice == "1":
        save_hashes(directory, hash_file)
        print("✅ Hashes saved successfully.")
    elif choice == "2":
        compare_hashes(directory, hash_file)
    else:
        print("❌ Invalid choice.")
