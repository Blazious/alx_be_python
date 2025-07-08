correct_username = "admin123"
correct_password = "395xzg"


max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username_input = input("Enter your username: ").strip()
    password_input = input("Enter your password: ").strip()


    if username_input == correct_username and password_input == correct_password:
        print(f"✅ Login Successful! Welcome, {username_input}.")
        break
    else:
        attempts += 1
        print("*** Invalid credentials ***")
        if attempts < max_attempts:
            print(f"Attempts remaining: {max_attempts - attempts}")
        else:
            print("❌ Access denied. Too many failed attempts.")
