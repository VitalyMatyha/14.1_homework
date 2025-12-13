from src.product import Product


def test_creation_log_mixin(capfd):
    product = Product("Test Product", "Product description", 100, 1)

    out, _ = capfd.readouterr()
    assert "Product" in out
    assert "name='Test Product'" in out
    assert "description='Product description'" in out
