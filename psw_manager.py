
master_psw = input('What is the master password? ')

# View password functionality
def view():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, psw = data.split('|')
            print('User:', user, '| Password:', psw)

# Add password functionality
def add():
    name = input('Acount Name: ')
    psw = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + psw + '\n')


