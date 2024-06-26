from abc import ABC, abstractmethod


class Basic(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def new_product(self, *args):
        pass


class Enter_info:

    def __init__(self, product, description, price, quantity):
        self.product = product
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}({self.product}, {self.description}, {self.price}, {self.quantity})"


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

    def __len__(self, products):
        count = 0
        for product in self.__products:
            count += product.quantity
        return count


    def __str__(self):
        """Название продукта, количество продуктов: 200шт"""
        return f"{self.name}, количество продуктов: {len(self)}"

    @classmethod
    def unique_products(cls, products: list) -> int:
        set_names = []
        for product in products:
            if str(product) not in set_names:
                set_names.append(product)
        return len(set_names)

    @property
    def products(self):
        """вывод списка"""
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @products.setter
    def products(self, product):
        """добавляет продукт"""
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")
        elif product.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством.")
        else:
            self.__products.append(product)

    @property
    def product_stat(self):
        """выводит Продукт, 80 руб. Остаток: 15 шт."""
        for product in self.__products:
            return Product(product.name, product.description, product.price, product.quantity)

    def average_price(self, products):
        try:
            total_price = sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return total_price




class Product(Basic, Enter_info):
    """Класс товаров: наименование, описание, цена, количество"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __add__(self, other):
        if not type(self) == type(other):
            raise ValueError("Продукты должны быть из одного класса.")
        elif self.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством.")
        else:
            return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        """Выводит инф-цю типа "Название продукта, 80 руб. Остаток: 15 шт.\""""
        return f"{self.name}, {str(self.__price)} руб. Остаток: {str(self.quantity)} шт."

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

    @price.deleter
    def price(self):
        if int(self.__price) <= 0:
            print("Цена введена некорректно")

    def func(self):
        pass


class Smartphone(Product):
    """Класс Смартфон (дочерний от Product): производительность, модель, объём вн. памяти, цвет"""

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Выводит инф-цю типа "Название продукта, 80 руб. Остаток: 15 шт.\""""
        return f"{self.name}, {str(self.__price)} руб. Остаток: {str(self.quantity)} шт."


class Lawn_grass(Product):
    """Класс Трава_газонная (дочерний от Product): страна-производитель, срок прорастания, цвет."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Выводит инф-цю типа "Название продукта, 80 руб. Остаток: 15 шт.\""""
        return f"{self.name}, {str(self.__price)} руб. Остаток: {str(self.quantity)} шт."
