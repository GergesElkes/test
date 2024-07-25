import os

def unsafe_function(user_input):
    # Vulnerable to command injection
    os.system(f'echo {user_input}')

if __name__ == "__main__":
    user_input = input("Enter something: ")
    unsafe_function(user_input)
