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


    @property
    def products(self):
        """Для следующего метода"""
        return self.__products


    @property
    def products_list(self):
        """достаёт параметры товара из класса продукт"""
        product_items = []
        for item in self.__products:
            product_items = Product(item.name, item.description, item.price, item.quantity)
        return product_items


    @products.setter
    def products(self, product_list):
        """добавляет продукт"""
        self.__products.append(product_list)


    @property
    def product_stat(self):
        """выводит Продукт, 80 руб. Остаток: 15 шт."""
        result = ''
        for item in self.__products:
            print(item)
            result += f'{item.name}, {item.request_price} руб. Остаток: {item.quantity} шт.\n'
        return result


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


    @property
    def price(self):
        """Геттер для цены"""
        return self.__price



    @classmethod
    def new_product(cls, product_data: dict):
        """Добавление нового продукта"""
        return cls(**product_data)


    @price.setter
    def price(self, price):
        """проверка цены"""
        if self.price > 0:
            self.__price = price
        else:
            print("Цена введена некорректно")
            return False

    @price.deleter
    def price(self):
        if int(self.__price) <= 0:
            print("Цена введена некорректно")
            return False
        else:
            return True
