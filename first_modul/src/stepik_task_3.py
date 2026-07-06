# Продвинутое использование  str.format()

# first_name = input()
# second_name = input()
# last_name = input()

# user_data = [first_name,second_name,last_name]

# print("Фамилия: {0[0]}, Инициалы: {0[1][0]}.{0[2][0]}.".format(user_data))

# name = input()
# price = input()
# currecy = input()

# data = {
#     "name":name,
#     "price":price,
#     "currecy":currecy
# }

# template = "Цена на товар \"{0[name]}\" составляет {0[price]} {0[currecy]}."
# print(template.format(data))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# x = input()
# y = input()

# p = Point(x,y)

# template = "Точка находится в координатах (X: {0.x}, Y: {0.y})"
# print(template.format(p))

# server_config = {'ip': '192.168.1.1', 'port': 8080}
# db_config = {'host': 'localhost', 'user': 'admin'}

# print("Сервер {server[ip]} работает на порту {server[port]}. База данных: {db[user]}@{db[host]}.".format(server = server_config,db = db_config))

movie = {
    'title': 'Матрица',
    'year': 1999,
    'genres': ['Фантастика', 'Боевик', 'Триллер']
}

print("{0[title]} ({0[year]}) - Основной жанр: {0[genres][0]}.".format(movie))