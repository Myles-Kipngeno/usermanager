from .user import User
from .utils import *

class Usermanager:
    def __init__(self):
     self.users = {}

    def register_user(self, username ,password, email):
       password = hash_password(password)
       if username in self.users:
          print(f"{self.username} already exist")
          return False
       self.users[username] = User(username, password, email)

       print("User registerted successfully")
       return True
    
    def login(self, username, password):
       user = self.users.get(username)
       if user and check_password(password, user.password):
          print("Login successfully")
          return "Login successful"
       
       print("Invalid credetials")
       return False
    
    def update_user(self, username, new_email=None, new_password=None):
       user = self.users.get(username)
       if not user:
          print("User not found")
          return False
       if new_email:
          user.email = new_email
       if new_password:
          hashed_password = hash_password(new_password)
          user.password = hashed_password
       print("User updated successfully.")
       return True
         
    def delete_user(self, username):
       if username in self.users:
          del self.users[username]
          print("User deleted successfully.")
          return True
       print("User not found.")
       return False
    
    def list_user(self):
        if not self.users:
            print("No users found")
        for user in self.users.values():
            print(user)