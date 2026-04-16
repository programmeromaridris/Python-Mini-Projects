import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")
  
  
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")
        
 
def main():
    while True:
        choice = input("Do you want to [1] create an account or [2] login? (Enter 'q' to quit): ")
        if choice == "1": 
            create_account()
        elif choice == "2":
            login()
        elif choice.lower() == "q":
            print("Goodbye!")
            break   
        else:
            print("Invalid choice. Please enter 1, 2, or q.")
            continue
        
if __name__ == "__main__":
    main()        