users = [
    {'username': 'admin', 'password': 'admin002'},
    {'username': 'ram', 'password': 'ram002'},
    {'username': 'sita', 'password': 'sita002'}
]



s_index = 0
username = input("Enter username: ")
password = input("Enter password: ")
for i in users:
    if username == users[s_index]['username']:
        if password == users[s_index]['password']:
            print('You are welcome!')
        else:
            print('Your password is wrong')
    else:
        print("your username is worng")
        exit()
    s_index += 1