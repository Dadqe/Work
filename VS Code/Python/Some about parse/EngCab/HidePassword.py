import getpass
password = getpass.getpass('Pass: ')
if password == '1234':
  print('Ok!')
elif password != '1234':
  print('Problem :( ')