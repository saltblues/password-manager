master_pwd = input("What is the master password? ")

def view():
    pass


def add():
    name = input("Account Name: ")
    pwd = input("Password ")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press Q to quit?? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue