def validate_password(password):
    if len(password) < 6:
        print("❌ Password must have at least 6 characters")
        return False
    
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        print("❌ Password must contain at least one number")
        return False
    
    has_capital = any(char.isupper() for char in password)
    if not has_capital:
        print("❌ Password must contain at least one capital letter")
        return False
    
    return True

def main():
    print("=== Password Validator ===")
    print("Password Conditions:")
    print("1. At least 6 characters")
    print("2. At least one number (0-9)")
    print("3. At least one capital letter (A-Z)")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Check Password")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            password = input("Enter password: ")
            print("\nChecking password...")
            if validate_password(password):
                print("✅ Password Accepted")
            else:
                print("❌ Password Invalid")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()