import itertools
from datetime import datetime

def set_password():
    while True:
        password = input("Set an 8-character password (for educational purposes): ")
        if len(password) == 8:
            return password
        else:
            print("Password must be exactly 8 characters.")

def brute_force_cracker(target_password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!$#@ '
    password_length = 8

    start_time = datetime.now()

    for attempt in itertools.product(characters, repeat=password_length):
        current_attempt = ''.join(attempt)
        print(f"Trying: {current_attempt}")

        if current_attempt == target_password:
            end_time = datetime.now()
            time_taken = end_time - start_time
            print(f"\nPassword found: {current_attempt}")
            print(f"Time taken: {time_taken}")
            return

    print("\nPassword not found.")

def password_strength_checker(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in "_-!$#@ " for char in password)
    has_digit = any(char.isdigit() for char in password)

    # Calculate strength
    strength_count = sum([has_lower, has_upper, has_special, has_digit])

    if strength_count == 4:
        return "strong"
    elif strength_count == 3:
        return "medium"
    elif strength_count == 2:
        return "weak"
    else:
        return "very weak"

def main():
    user_password = set_password()
    print(f"\nPassword strength: {password_strength_checker(user_password)}")
    brute_force_cracker(user_password)

if __name__ == "__main__":
    main()
