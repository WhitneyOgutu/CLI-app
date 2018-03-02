class Users (object):
    
    def __init__(self):
        self.users_list = []

    #user creat account
    def user_create_account(self, username, password):
        """ creating users in a dictionary"""
        user = {}
        user['username'] = username
        user['password'] = password
        #adding user to users_list
        self.users_list.append(user)
        return {'message': 'Account created'}