if __name__ == '__main__':

    birthdays = {'chay': '30/00/2000',
        'maggi': '08/09/1998',
        'kavi': '18/08/1977',
        'gs': '17/11/1971'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to know?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('we don\'t have {}\'s birthday.'.format(name))
