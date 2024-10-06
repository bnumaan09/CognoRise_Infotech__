import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Count the minimum number of required characters based on user choices
    min_required_characters = use_uppercase + use_lowercase + use_digits + use_special
    
    # Ensure the password length is not less than the number of required character types
    if length < min_required_characters:
        print(f"Error: Password length must be at least {min_required_characters} to include all selected character types.")
        return None

    # Start with an empty set of characters
    characters = ""
    password = []
    
    # Add character sets based on user's choices
    if use_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
        
    if use_lowercase:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
        
    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))
        
    if use_special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(characters))
    
    # Shuffle to prevent predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Check strength
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Moderate"
    else:
        return "Weak"

while True:
    # User input for password length
    length = int(input("Enter the desired length of the password: "))

    # User input for character types
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

    if generated_password:
        print(f"Generated Password: {generated_password}")
        # Display password strength
        print(f"Password Strength: {password_strength(generated_password)}")
    
    # Ask if user wants to generate another password
    another = input("Do you want to generate another password? (y/n): ").lower()
    if another != 'y':
        print("Goodbye!")
        break
