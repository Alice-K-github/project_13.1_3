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

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        """Название продукта, количество продуктов: 200шт"""
        return f"{self.name}, количество продуктов: {len(Category(self.name, self.description, self.products))}"

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
        self.__products.append(product)

    @property
    def product_stat(self):
        """выводит Продукт, 80 руб. Остаток: 15 шт."""
        for product in self.__products:
            return Product(product.name, product.description, product.price, product.quantity)


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

    def __add__(self, other):
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
