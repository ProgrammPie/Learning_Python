# name = input()
# age = int(input())
# balance = float(input())

# data = {
#     "name": name,
#     "age":age,
#     "balance":balance
# }

# template = "Пользователь %(name)s (возраст: %(age)d) имеет баланс %(balance)f руб."
# print(template % data)

sensor_id = input()
event_code = int(input())
temperature = float(input())

data = {
    "id":sensor_id,
    "code":event_code,
    "temp":temperature
}

template = "[LOG] Sensor: %(id)s | Event: %(code)04d | Temp: %(temp).1f C"
print(template % data)