def ask_password(login, password, success, failure):
    gl_letters = ['a', 'e', 'i', 'o', 'u', 'y']
    sogl_letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    sogl_letters_in_login = list(map(lambda x: x.lower() in sogl_letters, login))
    # gl_letters_in_login = list(map(lambda x: x.lower() in gl_letters, login))

    sogl_letters_in_password = list(map(lambda x: x.lower() in sogl_letters, password))
    gl_letters_in_password = list(map(lambda x: x.lower() in gl_letters, password))

    if (gl_letters_in_password.count(True) != 3) and (len(sogl_letters_in_login) != sogl_letters_in_password.count(True)):
        failure(login, "Everything is wrong")

    elif gl_letters_in_password.count(True) != 3:
        failure(login, "Wrong number of vowels")

    elif sogl_letters_in_login.count(True) != sogl_letters_in_password.count(True):
        failure(login, "Wrong consonants")

    else:
        success(login)


def main(login, password):
    success = lambda log: print(f'Привет {log}')
    failure = lambda log, mes: (
        print(f'Кто-то пытался притвориться пользователем {log}, но в пароле допустил ошибку: {mes}'))
    ask_password(login, password, success, failure)


main("anastasia", "nsyatos")
print()
main("eugene", "aanig")
print()
ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))
