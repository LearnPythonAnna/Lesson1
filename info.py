user_info = {'first_name': ' ', 'last_name': ' '}
print(user_info.get('first_name'))
user_info['first_name'] = input('Enter your name please: ')
user_info['last_name'] = input('Enter your surname please: ')
print(user_info)