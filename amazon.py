class amazon():
    users = {'abhi': 'nanda'}
    def __init__(self,username, password):            
                self.username = username
                self.password = password
                if self.username in amazon_users:
                    if amazon.users[self.usersname] == self.password:
                        print('login successful')
                    else:
                        print('incorrect password')
                else:
                    print("you don't have account")
                    con = input('Would you like to create an account(Y/N): ')
                    if con =='y':
                        username = input('username: ')
                        password = input('password: ')
                        amazon.users[username] = password
                        print('user added successfully')
                    else:                        
                        print('thanks for using')



new = amazon('kishore', 'pinnapuralla')                 
                         
                                                     
