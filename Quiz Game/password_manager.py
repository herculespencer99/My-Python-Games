from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", 
           fer.decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like to add a new password or view an existing one(add/view), press q to quit? ").lower()
    if mode == "q":
        break

    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
        continue