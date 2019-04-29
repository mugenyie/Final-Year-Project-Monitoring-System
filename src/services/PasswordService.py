import random, string

class GeneratePassword:
    """Generate random password or pin"""
    def generate_pin(self, length=6):
        return "".join(random.choice(string.digits) for i in range(length))
        
    def generate_password(self, length=6):
        return "".join(random.choice(string.ascii_letters) for i in range(length))