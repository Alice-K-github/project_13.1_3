class Category:
    """Класс категорий: наименование, описание, товар (+подсчёт всего категорий и продуктов)"""
    name: str
    description: str
    products: list
    all_category = 0
    unique_products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.all_category += 1
        Category.unique_products_count += Category.unique_products(self.__products)

    @classmethod
    def unique_products(cls, __products: list) -> int:
        set_names = []
        for product_ in __products:
            if str(product_.title) not in set_names:
                set_names.append(product_.title)
        return len(set_names)

    """Для следующего метода"""

    @property
    def products(self):
        return self.__products

    """достаёт параметры товара из класса продукт"""

    @property
    def products_list(self):
        product_items = []
        for item in self.__products:
            product_items = Product(item.name, item.description, item.price, item.quantity)
        return product_items

    """добавляет продукт"""

    @products.setter
    def products(self, product_list):
        self.__products.append(product_list)

    """выводит Продукт, 80 руб. Остаток: 15 шт."""

    @property
    def product_stat(self):
        for item in self.__products:
            return f"{item.name}, {item.price} руб. Остаток: {item.quantity} шт."


class Product:
    """Класс товаров: наименование, описание, цена, количество"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    """Геттер для цены"""

    @property
    def price(self):
        return self.__price

    """Ввод нового продукта"""

    @property
    def get_items(self):
        items = []
        product_name = input("Введите наименование: ")
        product_description = input("Введите описание: ")
        product_price = input("Укажите цену: ")
        product_quantity = input("Укажите количество: ")
        items.append(product_name + product_description + product_price + product_quantity)
        return items

    """Добавление нового продукта"""

    @classmethod
    def product(cls, get_items):
        items = get_items()
        name, description, price, quantity = items
        return cls(name, description, price, quantity)

    """проверка цены"""

    @price.setter
    def price(self, price):
        self.price = price

    @price.deleter
    def price(self):
        if int(self.__price) <= 0:
            print("Цена введена некорректно")
            return False
        else:
            return True
