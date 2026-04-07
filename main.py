from config import MAX_TRIES, PASSWORD

def login():
    tries = 0

    while tries < MAX_TRIES:
        user_input = input("Enter password: ")

        if user_input == PASSWORD:
            print("Login successful")
            return
        else:
            tries += 1
            remaining = MAX_TRIES - tries

            if remaining == 0:
                print("Too many requests. Exiting...")
            else:
                print(f"Wrong password. You have {remaining} tries left.")

if __name__ == "__main__":
    login()
