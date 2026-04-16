import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter a username:")
    password = getpass.getpass("Enter a password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")
  
  
create_account()