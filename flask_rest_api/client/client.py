import requests


#r = requests.get('http://127.0.0.1:5000/users')
#print(r.json())
#r = requests.post('http://127.0.0.1:5000/users', json={"id": 2, "name": "Kostya", "surname": 'Yorke'})
#print(r.json())



flag = True
id_on_server = 1
while(flag):
    print("Если хотите добавить нового пользователя введите 1\nЕсли хотите заменить данные существующего пользователя введите 2")
    print("Если хотите удалить существующего пользователя введите 3\nЕсли хотите завершить введите 0")
    user_number = int(input())
    if user_number == 0:
        flag = False

    elif user_number == 1:
        id_on_server += 1
        name = str(input("Введите имя пользователя (на английском): "))
        surname = str(input("Введите фамилию пользователя (на английском): "))
        r = requests.post('http://127.0.0.1:5000/users', json={"id": id_on_server, "name": name, "surname": surname})

    elif user_number == 2:
        id = int(input("Введите id пользователя, которого хотите заменить: "))
        name = str(input("Введите имя пользователя (на английском): "))
        surname = str(input("Введите фамилию пользователя (на английском): "))
        r = requests.put('http://127.0.0.1:5000/users', json={"id": id, "name": name, "surname": surname})

    elif user_number == 3:
        id = int(input("Введите id пользователя, которого хотите удалить: "))
        r = requests.delete('http://127.0.0.1:5000/users', json={"id": id})