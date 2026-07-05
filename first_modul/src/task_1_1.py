def price_counter()->str:
    price = float(input("Введите стоимость одного товара:"))
    amount = int(input("Введите количество товара:"))

    if price*amount >= 1000:
        return f"Итого: {price*amount*0.9:_} ₽"
    
    return f"Итого: {price*amount:_} ₽"

print(price_counter())
# print(f"{255:016b}")