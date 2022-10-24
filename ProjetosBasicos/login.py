import time

#pagina de login em python basica!

username = "admin"
password = "admin"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print('Analisando...')
    print('Aguarde...')
    time.sleep(5)
    print('loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Login Aprovado! redirecionando para pagina inicial.')

else:
    print('Loading...')
    time.sleep(3)
    print('...')
    time.sleep(1)
    print('Username ou senha incorreto!')
    print('Tente novamente!')
