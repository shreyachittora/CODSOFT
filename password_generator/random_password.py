import string
import random

def random_pass(pass_length, s1,s2,s3,s4):
    string_main = []
    string_main.extend(list(s1))
    string_main.extend(list(s2))
    string_main.extend(list(s3))
    string_main.extend(list(s4))

    random.shuffle(string_main)
    password = ''.join(string_main[0:pass_length])
    return password


if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

# keeps on inputting till the pass_length is not a valid integer entered
    while True:
            try:
                pass_length = int(input("Enter the length you want for your password: "))
                if pass_length <= 0:
                    print("Please enter a positive integer.")
                    continue
                break  # Exit the loop if input is a valid integer
            except ValueError:
                print("The variable is not an integer. Please enter a valid integer.")

password = random_pass(pass_length, s1,s2,s3,s4)

print(f"Your random password is : {password}")


