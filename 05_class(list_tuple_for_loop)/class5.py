database : list[tuple[str, str]] = [("amina12345", "90078601"),
                                    ("sabeeha000", "247365"),
                                    ("anzish159", "951159")]

user_name : str = input("Enter your username: ")
user_password : str = input("Enter your password: ")

for row in database:
    username , userpassword = row
    if user_name == username and user_password == userpassword:
        print(f'Valid user: {username}')
        break
else:
        print('Invalid credentials')