def collect(**kwargs):
    """
    Возвращает данные о пользователе в одну строку
    :param kwargs: {name:'value', surname:'value', year:'value', city:'value', email:'value', phone:'value'}
    :return: str
    """
    print(f"Имя пользователя: {kwargs['name']}, "
          f"фамилия пользователя: {kwargs['surname']}, "
          f"год рождения: {kwargs['year']}, "
          f"город проживания: {kwargs['city']}, "
          f"email: {kwargs['email']}, "
          f"phone: {kwargs['phone']}")


collect(name=input("Введите имя: "),
        surname=input("Введите фамилию: "),
        year=input("Введите год рождения: "),
        city=input("Введите город проживания: "),
        email=input("Введите email: "),
        phone=input("Введите номер телефона: "),
        )
