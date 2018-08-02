import getpass

password = getpass.getpass('Please enter your password:')
while password != ('hello'):
    print('Wrong password')
    password=getpass.getpass('Type again:')
    
