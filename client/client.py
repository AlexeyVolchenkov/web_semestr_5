import requests


flag = True
while(flag):
    print("Если хотите добавить нового пользователя введите 1\nЕсли хотите заменить данные существующего пользователя введите 2")
    print("Если хотите удалить существующего пользователя введите 3\nЕсли хотите завершить введите 0")
    user_number = str(input()).replace(" ", "")
    if user_number == 0:
        flag = False

    elif user_number == "1":
        name = str(input("Введите имя пользователя (на английском): ")).replace(" ", "")
        surname = str(input("Введите фамилию пользователя (на английском): ")).replace(" ", "")
        r = requests.post('http://127.0.0.1:5000/users', json={"name": name, "surname": surname})

    elif user_number == "2":
        user_id = int(str(input("Введите id пользователя, которого хотите заменить: ")).replace(" ", ""))
        name = str(input("Введите имя пользователя (на английском, если не хотите менять этот параметр, то оставьте поле пустым): ")).replace(" ", "")
        surname = str(input("Введите фамилию пользователя (на английском, если не хотите менять этот параметр, то оставьте поле пустым): ")).replace(" ", "")
        r = requests.put('http://127.0.0.1:5000/users', json={"id": user_id, "name": name, "surname": surname})

    elif user_number == "3":
        user_id = int(str(input("Введите id пользователя, которого хотите удалить: ")).replace(" ", ""))
        r = requests.delete('http://127.0.0.1:5000/users', json={"id": user_id})