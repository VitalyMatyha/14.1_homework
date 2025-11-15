from src import category
from src.category import Category
from src.product import Product

def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 2