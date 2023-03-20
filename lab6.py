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

def decoder(password):
    end_result = ''
    for i in range(len(password)):  # iterates through index
        a = int(password[i])  # get integer value at index

        b = a - 3  # decrement by 3
        b = str(b)
        end_result += b  # add back to original password
    return end_result

if __name__ == "__main__":
    menu = True
    while menu:
        print_menu()
        print("Please enter an option:", end = " ")
        option = int(input())
        if option == 1:
            # encodes password input
            password = input("Please enter your password to encode:")
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            # decodes and prints the existing encoded password
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.")
        elif option == 3:
            menu = False
