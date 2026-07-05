# str.format()

# name = input()
# age = int(input())
# city = input()

# print("Пользователь {} из города {} имеет возраст {}.".format(name,city,age))

# name = input()
# color = input()

# print("Любимый цвет пользователя {0} - {1}. {1} - очень красивый!".format(name,color))

# char_name = input()
# char_class = input()
# char_level = int(input())
# char_hp = int(input())

# print("Персонаж {name} (Класс: {Class}, Уровень: {lvl}) имеет {HP} 
# очков здоровья.".format(name=char_name,Class = char_class,lvl = char_level,HP = char_hp))

# timestamp = input()
# action = input()
# username = input()
# status = input()

# print("[{timestamp}] Action: {} | User: {} | Status: {}".format(action,username,status,timestamp = timestamp))

title = input()
author = input()
pages = int(input())
year = int(input())

print("Книга '{title}', автор {author}".format(title = title,author = author))
print("Автор {author} написал книгу '{title}' в {year} году." \
" Количество страниц: {pages}.".format(author = author,year = year, pages= pages,title = title))