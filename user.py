#6
class User:
    def __init__(self,username,email,is_active):
        self.username=username
        self.email=email
        self.is_active=is_active

    def update_email(self,new_email):
        if not '@' in new_email:
            pass
        else:
            self.email=new_email

    def deactivate(self):
        if self.is_active == 'inactive':
            pass
        else:
            print('inactive')

    def get_info(self):
        self.update_email('wwwwwgmail.com')
        return f"{self.username.lower()}: {self.email}, {self.is_active}"

user1 = User('botirbek','abotirbek@gmail.com','active')
print(user1.get_info())
print(user1.deactivate())