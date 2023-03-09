def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")


def encode(password):
    new_string = ""  # initialize encoded password
    for i in range(len(password)):  # get index
        a = int(password[i])
        b = a + 3  # increment by 3
        b = str(b)
        new_string += b  # add to the encoded password
    return new_string


if __name__ == "__main__":
    menu = True
    while menu:
        print_menu()
        print("Please enter an option:", end = " ")
        option = int(input())
        if option == 1:
            password = input("Please enter your password to encode:")
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            # print(f"The encoded password is {encoded_pw}, and the original password is {password}.")
            pass
        elif option == 3:
            menu = False
