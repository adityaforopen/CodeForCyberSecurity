import hashlib
import requests
import os

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def password_cracker(sha1_hash, use_salts=False):
    # Prompt the user for the password file link or upload
    password_file_input = input("Enter the link of the password file or upload the file (leave blank to skip): ")
    if password_file_input:
        download_file(password_file_input, 'top-10000-passwords.txt')
        password_file = 'top-10000-passwords.txt'
    else:
        password_file = input("Enter the path to the password file: ")

    # Prompt the user for the salts file link or upload
    salts_file_input = input("Enter the link of the salts file or upload the file (leave blank to skip): ")
    if salts_file_input:
        download_file(salts_file_input, 'known-salts.txt')
        salts_file = 'known-salts.txt'
    else:
        salts_file = input("Enter the path to the salts file: ")

    # Load the top 10,000 passwords
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    # Load the known salts if use_salts is True
    salts = []
    if use_salts:
        with open(salts_file, 'r') as file:
            salts = file.read().splitlines()

    # Iterate through each password and salt combination
    for password in passwords:
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
        if hashed_password == sha1_hash:
            return password
        if use_salts:
            for salt in salts:
                hashed_password_with_salt = hashlib.sha1((salt + password + salt).encode()).hexdigest()
                if hashed_password_with_salt == sha1_hash:
                    return password
    return "PASSWORD NOT IN DATABASE"

if __name__ == "__main__":
    sha1_hash = input("Enter the SHA-1 hash: ")
    use_salts = input("Use salts? (True/False): ").lower() == 'true'
    print(password_cracker(sha1_hash, use_salts))
