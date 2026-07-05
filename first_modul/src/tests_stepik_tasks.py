from stepik_tasks import first_task

def first_task_test()->None:
    assert first_task("Иван",30,"Москва") == "Пользователь Иван, возраст 30, живет в городе Москва."

def first_task_zero_test()->None:
    assert first_task() == "Пользователь  , возраст  , живет в городе  ."