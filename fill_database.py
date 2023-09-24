from loader import db, default_image
import random

db.add_user("test1", "123456789")
db.add_user("test2", "1234", True)
db.add_user("1", "1", True)
db.add_user("car", "car")


db.add_category("Роман")
db.add_category("Научная фантастика")
db.add_category("История")
db.add_category("Детектив")
db.add_category("Фэнтези")
db.add_category("Наука")
db.add_category("Путешествия")
db.add_category("Биография")
db.add_category("Поэзия")
db.add_category("Философия")


# Романы
db.add_book("Великий Гэтсби", "Ф. Скотт Фицджеральд", 1925, "История о потерянном поколении", 300, 1, ".\\images\\cover1__w600.jpg")
db.add_book("Анна Каренина", "Лев Толстой", 1877, "История любви и предательства", 500, 1, ".\\images\\172100.jpg")
db.add_book("На переломе", "Эрих Мария Ремарк", 1931, "История о послевоенной Германии", 400, 1, ".\\images\\erih-mariya-remark-na-zapadnom-fronte-bez-peremen.jpg")

# Научная фантастика
db.add_book("Дюна", "Фрэнк Герберт", 1965, "Борьба за пустынную планету", 450, 2, ".\\images\\10916281_0.jpg")
db.add_book("1984", "Джордж Оруэлл", 1949, "Антиутопия о тоталитарном обществе", 350, 2, ".\\images\\81StSOpmkjL._AC_UF1000,1000_QL80_.jpg")
db.add_book("Эндер", "Орсон Скотт Кард", 1985, "Тренировка юного генерала", 370, 2, ".\\images\\Orson_Skott_Kard__Igra_Endera._Govoryaschij_ot_imeni_mertvyh._Rasskazy_sbornik.jpg")


# История
db.add_book("История Рима", "Тит Ливий", -30, "Описывает историю Рима с мифического основания до начала Империи", 550, 3, ".\\images\\6042731886.jpg")
db.add_book("Война и мир", "Лев Толстой", 1869, "Эпический роман о Наполеоновских войнах", 700, 3, ".\\images\\i741097.jpg")
db.add_book("Короткая история человечества", "Юваль Ной Харари", 2011, "С момента появления Homo sapiens и до наших дней", 420, 3, ".\\images\\22150614.jpg")

# Детектив
db.add_book("Убийство в \"Восточном экспрессе\"", "Агата Кристи", 1934, "Одно из самых знаменитых расследований Пуаро", 320, 4, ".\\images\\18922333.jpg")
db.add_book("Собака Баскервилей", "Артур Конан Дойль", 1902, "Шерлок Холмс расследует таинственное проклятие", 310, 4, ".\\images\\96467.jpg")
db.add_book("Девушка с татуировкой дракона", "Стиг Ларссон", 2005, "Журналист и хакер расследуют преступление", 330, 4, ".\\images\\The_Girl_with_the_Dragon_Tatoo.jpg")

# Фэнтези
db.add_book("Властелин колец", "Дж. Р. Р. Толкин", 1954, "Эпическая история о кольце всевластья", 500, 5, default_image)
db.add_book("Игра престолов", "Джордж Мартин", 1996, "Борьба за Железный трон Вестероса", 490, 5, default_image)
db.add_book("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, "Первый роман о юном волшебнике", 350, 5, default_image)

# Наука
db.add_book("Краткая история времени", "Стивен Хокинг", 1988, "О черных дырах и происхождении вселенной", 400, 6, default_image)
db.add_book("Самые красивые теории", "Жан-Пьер Лумине", 2011, "Об истории научных открытий", 380, 6, default_image)
db.add_book("Гены, народы и языки", "Лука Кавалли-Сфорца", 2000, "О генетическом происхождении человечества", 410, 6, default_image)

# Путешествия
db.add_book("Вокруг света за 80 дней", "Жюль Верн", 1873, "Путешествие Филиаса Фогга", 340, 7, default_image)
db.add_book("Путешествие к центру Земли", "Жюль Верн", 1864, "Опускаясь в глубины земной коры", 330, 7, default_image)
db.add_book("Дорогами Сибири", "Сильвен Тессон", 2010, "Путешествие по заснеженной Сибири", 350, 7, default_image)

# Биография
db.add_book("Стив Джобс", "Уолтер Айзексон", 2011, "Биография основателя Apple", 460, 8, default_image)
db.add_book("Диарея молодой девушки", "Анна Франк", 1947, "Жизнь в скрытности во время Второй мировой войны", 290, 8, default_image)
db.add_book("Леонардо да Винчи", "Уолтер Айзексон", 2017, "Исследование жизни великого гения", 480, 8, default_image)

# Поэзия
db.add_book("Сонеты", "Уильям Шекспир", 1609, "Коллекция из 154 сонетов", 250, 9, default_image)
db.add_book("Лирика", "Анна Ахматова", 1917, "Стихи великой русской поэтессы", 240, 9, default_image)
db.add_book("Стихи", "Роберт Фрост", 1916, "Избранные стихи американского поэта", 230, 9, default_image)


# Философия
db.add_book("Бытие и время", "Мартин Хайдеггер", 1927, "Философский трактат", 600, 10, default_image)
db.add_book("Мир как воля и представление", "Артур Шопенгауэр", 1819, "Основные идеи философии Шопенгауэра", 700, 10, default_image)
db.add_book("Критика чистого разума", "Иммануил Кант", 1781, "Основополагающий труд Канта", 650, 10, default_image)


def add_sample_orders(num_orders=30):
    users = db.get_all_users()

    if not users:
        print("No users in the database!")
        return

    addresses = ["Main St.", "Elm St.", "Park Ave.", "Broadway", "5th Ave."]
    emails = ["example@example.com", "test@test.com", "user@domain.com"]
    phone_numbers = ["555-1234", "555-5678", "555-8765"]
    payment_types = [1, 2, 3]  # Предположим, что 1, 2 и 3 представляют разные типы оплаты

    books = db.get_all_books()  # получаем все книги из базы данных

    if not books:
        print("No books in the database!")
        return

    for _ in range(num_orders):
        user_id = random.choice(users)[0]  # Выбираем случайного пользователя
        price = round(random.uniform(10, 500), 2)  # Случайная цена от 10 до 500
        address = random.choice(addresses)
        email = random.choice(emails)
        phone = random.choice(phone_numbers)
        payment_type = random.choice(payment_types)

        order_id = db.add_order(user_id, price, address, email, phone, payment_type)

        # Добавляем случайные элементы заказа (от 1 до 5 элементов)
        for _ in range(random.randint(1, 5)):
            book = random.choice(books)  # выбираем случайную книгу
            book_id = book[0]
            quantity = random.randint(1, 5)  # Количество от 1 до 5
            db.add_order_item(order_id, book_id, quantity)


add_sample_orders()
