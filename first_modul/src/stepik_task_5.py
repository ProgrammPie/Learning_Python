# from string import Template

# temp = input()
# user = input()
# id = input()

# data = {
#     "user":user,
#     "order_id":id
# }

# template = Template(temp)
# print(template.substitute(data))

# key,value = input(),input()

# print(f'{{ "{key}":  "{value}" }}')

# user_id = int(input())
# user_status = input()

# print(f"DEBUG: {user_id=}, {user_status=}")

# import datetime
# event_time = datetime.datetime(2025, 10, 26, 10, 30, 0)

# print(f"Дата: {event_time:%d.%m.%Y}")
# print(f"Время события: {event_time:%H:%M:%S}")

import datetime
report_date = datetime.date(2025, 7, 5)

print(f"report_{report_date:%Y_%m_%d}.csv")