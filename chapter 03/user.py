class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def verify_password(self, password):
        if password == self.__password:
            print("Password is correct.")
            return True
        else:
            print("Password is incorrect.")
            return False
        
    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.__password = new_password
            print("Password has been changed successfully.")
        else:
            print("Failed to change password. Old password is incorrect.")


 # Example of Private Access to attributes
user1 = User("john_doe", "securepassword123")
print(f"1. {user1.verify_password('securepassword123')}")  # Correct password
print(f"2. {user1.verify_password('wrongpassword')}") # Incorrect password
print(f"3. {user1.change_password('securepassword123', 'newsecurepassword456')}")  # Change password with correct old password
print(f"4. {user1.verify_password('newsecurepassword456')}")  # Verify new password
print(f"5. {user1.change_password('wrongpassword', 'anotherpassword789')}")  # Attempt to change password with incorrect old password

