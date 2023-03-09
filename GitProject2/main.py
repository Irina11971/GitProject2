import random
import string

def creating_password (login: str) ->str:
    """
    Создание пароля для нового пользователя

    :param login (str): логин
    :return:
            str: пароль
    """

    password = ""
    length = 16

    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    for i in range(length):
        number_list = random.randint(1, 5)
        if (number_list == 1 or number_list == 2):
            password += letters[random.randint(0, len(letters) - 1)]
        elif (number_list == 3 or number_list == 4):
            password += numbers[random.randint(0, len(numbers) - 1)]
        else:
            password += symbols[random.randint(0, len(symbols) - 1)]

    return password

def execute_application(): # основная программа

    with open("file.txt", "r", encoding="UTF-8") as file:
        text = file.readlines()
    login = ""
    while (True):
        try:
            login = input("Введите логин: ")
            assert len(login) <= 16, f"Логин не может состоять более, чем из 16 символов"
            for line in text:
                line = line.rstrip('\n')
                line = line.split()
                for word in line:
                    if word == login:
                        raise Exception(f"Такой логигин уже зарегистрирован")
            break
        except Exception as e:
            print(e)
        except Exception as e:
            print(e)

    while (True):
        ispassword = True
        password = creating_password(login)
        for line in text:
            line = line.rstrip('\n')
            line = line.split()
            for word in line:
                if word == password:
                    ispassword = False
                    break
            break
        if ispassword:
            break

    print(f"Ваш пароль {password}")
    user_password = login + " " + password + '\n'

    with open("file.txt", "a", encoding="UTF-8") as file:
        file.write(user_password)


if __name__ == "__main__":
    execute_application()












