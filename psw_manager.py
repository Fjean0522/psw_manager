
master_psw = input('What is the master password? ')

# View and Add password functionality
def view():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, psw = data.split('|')
            print('User:', user, '| Password:', psw)



