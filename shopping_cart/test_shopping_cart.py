import unittest
from shopping_cart import Item, ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)
    

    def tearDown(self):
        pass

    def test_cinco(self):
        assert 5 + 5 == 10

    def test_nombre(self):
        self.assertEqual(self.pan.name, "Pan")

    def test_nombre_no_igual(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_productoO(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)


if __name__ == '__main__':
    unittest.main()
