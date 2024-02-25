import pytest

from src.functions import Category, Product


@pytest.fixture
def category_name():
    """Проверка инициализации объектов класса Category"""
    return Category("имя", "описание", ["продукт", "продукт2"])


def test_init_category(category_name):
    assert category_name.name == "имя"
    assert category_name.description == "описание"
    assert category_name.products == ["продукт", "продукт2"]
    assert category_name.all_category == 1
    assert category_name.unique_products_count == 2


"""Проверка инициализации объектов класса Product"""


@pytest.fixture
def product_category():
    return Product("имя", "описание", 134.50, 3)


def test_init_product(product_category):
    assert product_category.price == 134.50
    assert product_category.quantity == 3
    assert product_category.name == "имя"
    assert product_category.description == "описание"


def test_category_count():
    """Проверка подсчёта"""
    assert Category.all_category == 1

    Category("name", "description", ["apple", "pine"])
    assert Category.all_category == 2

    Category("name_1", "description", ["apple", "pine", "pine"])
    assert Category.all_category == 3
