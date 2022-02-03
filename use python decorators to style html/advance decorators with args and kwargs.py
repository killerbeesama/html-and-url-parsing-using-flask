
def deco(func):
    def wraper(*args):
        if args[0].is_logged_in == True:
            func(args[0])
    return wraper

class User:
    def __init__(self,name) -> None:
        self.name = name
        self.is_logged_in = False
    
@deco
def create_post(user):
    print(f"This is {user.name}'s new post")

new_user = User("user")
new_user.is_logged_in = True
create_post(new_user)
