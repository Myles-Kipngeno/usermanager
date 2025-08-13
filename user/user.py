class User:
    def __init__(self, username, email, password):
        self.usernamr = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"User: {self.username} , Email: {self.email}"
    

