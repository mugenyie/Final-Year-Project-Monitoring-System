import random, string

class GeneratePassword:
    """Generate random password or pin"""
    __password_choice = string.digits + string.ascii_letters + string.punctuation
    
    def generate_pin(self, length=6):
        return "".join(random.choice(string.digits) for i in range(length)) 

    def generate_password(self, length=6):
        return "".join(random.choice(__password_choice) for i in range(length))